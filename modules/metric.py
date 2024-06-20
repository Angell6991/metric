 ############################################################
##############################################################
###                                                        ###
###   AAAAAA   NN      NN   GGGGGG    EEEEEE   ||    ||    ###
###  AAAAAAAA  NNN     NN  GGGGGGGG  EEEEEEEE  ||    ||    ###
###  AA    AA  NNNN    NN  GG        EE        ||    ||    ###
###  AA    AA  NNNNN   NN  GG        EE        ||    ||    ###
###  AAAAAAAA  NN NNN  NN  GG  GGG   EEEEEEEE  ||    ||    ###
###  AAAAAAAA  NN   NNNNN  GG  GGGG  EE        ||    ||    ###
###  AA    AA  NN    NNNN  GG    GG  EE        ||    ||    ###
###  AA    AA  NN     NNN  GGGGGGGG  EEEEEEEE  ||||  ||||  ###
###  AA    AA  NN      NN   GGGGGG    EEEEEE   ||||  ||||  ###
###                                                        ###
##############################################################
 ############################################################

import sympy as sy
import pandas as pd

##############################################################
###------------------Guia_de_funciones---------------------###
##############################################################
###                                 |                      ###
###   Tensor metrico                |   metric()           ###
###   T metrico inverso             |   metric_inv()       ###
###   Simb Christofell clase 1      |   Christofell(k)     ###
###   Simb Christofell Clase 2      |   Conexion(k)        ###
###   T Riemann 4-Cova              |   riemann(i,j)       ###
###   T Riemann 3-Cova y 1-Contrava |   Riemann(i,j)       ###
###   T Ricci                       |   Ricci()            ###
###   Escalar de Curvatura          |   EscalarC()         ###
###                                 |                      ###
##############################################################
##############################################################

class metric_dat:

    def __init__(self, variables, no_variables, Tensor_metric):
        
        #------------------------Insert_data-------------------------#
        
        #---------------------Insert_variables-----------------------#
        self.lista1      =      pd.read_csv(variables, header = None)
        self.lista1      =      self.lista1.values.tolist()
        self.n           =      len(self.lista1)
        
        self.var         =      []
        for i in range(self.n):
            self.var.append(sy.symbols(self.lista1[i][0]))
        
        self.var         =      sy.Array(self.var)
            

        #----------------------Insert_constants----------------------#
        self.lista2     =       pd.read_csv(no_variables, header = None)
        self.lista2     =       self.lista2.values.tolist()
        
        self.varr       =       []
        for i in range(len(self.lista2)):
            self.varr.append(sy.symbols(self.lista2[i][0]))
        
        self.varr       =      sy.Array(self.varr)


        #--------------------Insert_tensor_metric--------------------#
        self.lista3     =       pd.read_csv(Tensor_metric, header = None)
        self.lista3     =       self.lista3.values.tolist()

        
        ##############################################################
        ##--------------Tensor_Metrico_y_inverso--------------------##
        ##############################################################

        #--------------------Tensor_metrico--------------------------#

        self.A   =  []
        self.itera  =   0
        for i in range(self.n):
            for j in range(self.n):
                if i <= j:
                    self.A.append(self.lista3[self.itera][0])
                    self.itera   =   self.itera + 1
                elif i > j:
                    self.A.append(0)
        self.A   =   sy.Array(self.A,(self.n,self.n))


        self.B   =  []
        for i in range(self.n):
            for j in range(self.n):
                if i > j:
                    self.B.append(self.A[j,i])
                elif i <= j:
                    self.B.append(0)
        self.B   =   sy.Array(self.B, (self.n,self.n))


        self.g   =    self.A + self.B
        self.G   =    sy.Array(self.g)


        #---------------Tensor_metrico_inverso-----------------------#
        self.Ginv  =    sy.simplify(sy.factor(sy.Matrix(self.G).inv()))
        self.Ginv  =    sy.Array(self.Ginv)


        ##############################################################
        ##----------Simbolos_de_Christofell_Clase_1-----------------##
        ##############################################################

        def christofell(k,j,i):
            ch  =   (
                    sy.diff(self.G[j,k],self.var[i]) + 
                    sy.diff(self.G[i,k],self.var[j]) - 
                    sy.diff(self.G[i,j],self.var[k]) 
                    )/2 
            return ch


        self.VChristofell_up      =   []
        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    if j <= i: 
                        self.VChristofell_up.append(christofell(k,j,i))
                    elif j > i:
                        self.VChristofell_up.append(0)
        self.VChristofell_up    =   sy.Array(self.VChristofell_up, (self.n, self.n ,self.n))
        

        self.VChristofell_dowm    =   []
        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    if j <= i: 
                        self.VChristofell_dowm.append(0)
                    elif j > i:
                        self.VChristofell_dowm.append(self.VChristofell_up[k,i,j])
        self.VChristofell_dowm  =   sy.Array(self.VChristofell_dowm, (self.n, self.n ,self.n))


        self.VChristofell       =   self.VChristofell_up    +   self.VChristofell_dowm


        ##############################################################
        ##-----------Simbolos_de_Christofell_Clase_2----------------##
        ##############################################################

        def conexion(i,j,k):
            cx   =   0
            for p in range(self.n):
                D    =   self.Ginv[k,p]*self.VChristofell[p,j,i] 
                cx   =   cx + D
                #cx   =   simplify(factor(cx + D)) 
            return cx


        self.VConexion_up       =   []
        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    if j <= i:
                        self.VConexion_up.append(conexion(i,j,k)) 
                    elif j > i:
                        self.VConexion_up.append(0)
        self.VConexion_up       =   sy.Array(self.VConexion_up, (self.n, self.n, self.n))


        self.VConexion_dowm     =   []
        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    if j <= i:
                        self.VConexion_dowm.append(0)
                    elif j > i:
                        self.VConexion_dowm.append(self.VConexion_up[k,i,j]) 
        self.VConexion_dowm     =   sy.Array(self.VConexion_dowm, (self.n, self.n, self.n))
        

        self.VConexion          =   self.VConexion_up    +   self.VConexion_dowm


        #############################################################
        ##----------Tensor_de_Riemann_4-Covariante-----------------##
        #############################################################

        def DD(p,i,j,k):
            D   =   0 
            for s in range(self.n):
                D   =   (
                        D + self.VConexion[s,k,p]*self.VChristofell[s,i,j] 
                        - self.VConexion[s,j,p]*self.VChristofell[s,i,k]
                        )
                D   =   sy.simplify(sy.factor(D))
            return D


        self.Vriemann_up     =   []
        for p in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        if p == i:
                            self.Vriemann_up.append(0)
                        elif j == k:
                            self.Vriemann_up.append(0)
                        elif j < k:
                            self.SS  =   (
                                    sy.diff(self.VChristofell[p,i,k], self.var[j]) - 
                                    sy.diff(self.VChristofell[p,i,j], self.var[k]) + 
                                    DD(p,i,j,k)
                                    )
                            self.SS  =   sy.simplify(sy.factor(self.SS))
                            self.Vriemann_up.append(self.SS)
                        elif j > k:
                            self.Vriemann_up.append(0)
        self.Vriemann_up     =   sy.Array(self.Vriemann_up, (self.n, self.n, self.n, self.n))


        self.Vriemann_dowm     =   []
        for p in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        if p == i:
                            self.Vriemann_dowm.append(0)
                        elif j == k:
                            self.Vriemann_dowm.append(0)
                        elif j < k:
                            self.Vriemann_dowm.append(0)
                        elif j > k:
                            self.Vriemann_dowm.append((-1)*self.Vriemann_up[p,i,k,j])
        self.Vriemann_dowm   =   sy.Array(self.Vriemann_dowm, (self.n, self.n, self.n, self.n))


        self.Vriemann     =   self.Vriemann_up     +   self.Vriemann_dowm 


        #############################################################
        ##-----Tensor_de_Riemann_3-Covariante_1-Contravariante-----##
        #############################################################

        def TRiemann(p,i,j,k):
            TT  =   0
            for s in range(self.n):
                TT  =   TT + self.Ginv[p,s]*self.Vriemann[s,i,j,k]
                TT  =   sy.simplify(sy.factor(TT))
            return TT


        self.VRiemann_up     =   []
        for p in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        if j < k:
                            self.VRiemann_up.append(TRiemann(p,i,j,k))
                        elif j >= k: 
                            self.VRiemann_up.append(0)
        self.VRiemann_up     =   sy.Array(self.VRiemann_up, (self.n, self.n, self.n, self.n))


        self.VRiemann_dowm     =   []
        for p in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        if j < k:
                            self.VRiemann_dowm.append(0)
                        elif j >= k:
                            self.VRiemann_dowm.append((-1)*self.VRiemann_up[p,i,k,j])
        self.VRiemann_dowm     =   sy.Array(self.VRiemann_dowm, (self.n, self.n, self.n, self.n))

        
        self.VRiemann     =   self.VRiemann_up      +   self.VRiemann_dowm


        #############################################################
        ##-------------------Tensor_de_Ricci-----------------------##
        #############################################################

        def ricci(i,j):
            ri  =   0
            for s in range(self.n):
                ri  =   ri + self.VRiemann[s,i,s,j]
                ri  =   sy.simplify(sy.factor(ri))
            return ri


        self.VRicci_up   =   []
        for i in range(self.n):
            for j in range(self.n):
                if j <= i:
                    self.VRicci_up.append(ricci(i,j))
                elif j > i: 
                    self.VRicci_up.append(0)
        self.VRicci_up   =   sy.Array(self.VRicci_up, (self.n, self.n))

        self.VRicci_dowm   =   []
        for i in range(self.n):
            for j in range(self.n):
                if j <= i:
                    self.VRicci_dowm.append(0)
                elif j > i:
                    self.VRicci_dowm.append(self.VRicci_up[i,j])
        self.VRicci_dowm   =   sy.Array(self.VRicci_dowm, (self.n, self.n))

        
        self.VRicci   =   self.VRicci_up        +   self.VRicci_dowm


        #############################################################
        ##-----------------Escalar_de_Curvatura--------------------##
        #############################################################

        self.VEscalarC = 0
        for i in range(self.n):
            for j in range(self.n):
                self.VEscalarC    =   self.VEscalarC + self.Ginv[i,j]*self.VRicci[i,j]
                self.VEscalarC    =   sy.simplify(sy.factor(self.VEscalarC)) 


    ##############################################################
    ##--------Definicion_de_funciones_en_forma_matricial--------##
    ##############################################################

    def metric(self):
        return self.G 

    def metric_inv(self):
        return self.Ginv

    def Christofell(self,k):
        return self.VChristofell[k]

    def Conexion(self,k):
        return self.VConexion[k]

    def riemann(self,j,i): 
        return self.Vriemann[j,i]

    def Riemann(self,j,i):
        return self.VRiemann[j,i]

    def Ricci(self):
        return self.VRicci 

    def EscalarC(self):
        return self.VEscalarC


#------------------------------------------------------------#

#--------------------instanciando_objeto---------------------#

import time
import os

os.system("clear")

variables       =   "~/.config/metric/support_files/intro_data/variables.dat"
no_variables    =   "~/.config/metric/support_files/intro_data/no_variables.dat"
tensor_metrico  =   "~/.config/metric/support_files/intro_data/tensor_metrico.dat"

start_time = time.time()                     # inicio del calculo, toma el tiempo inicial

inst  =   metric_dat(variables, no_variables, tensor_metrico)
# inst  =   metric_dat("variables.dat","no_variables.dat","tensor_metrico.dat")


print("tensor metrico")
print(inst.metric(), "\n")

print("tensor metrico inverso")
print(inst.metric_inv(), "\n")

print("simbolo de christofell")
print(inst.Christofell(0), "\n")

print("conexion")
print(inst.Conexion(1), "\n")

print("tensor de riemann")
print(inst.riemann(0,2), "\n")

print("tensor de Riemann")
print(inst.Riemann(0,1), "\n")

print("tensor de Ricci")
print(inst.Ricci(), "\n")

print("Escalar de curvatura")
print(inst.EscalarC())


end_time = time.time()                      # fin del calculo, toma tiempo final 

elapsed_time = end_time - start_time        # Tiempo que tarda en hacer los calculos  
print(f"El tiempo de ejecución fue: {elapsed_time} segundos")



