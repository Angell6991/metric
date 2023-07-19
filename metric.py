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
import os

##############################################################
##-------------------Guia_de_funciones----------------------##
##############################################################
##                                    |                     ##
##   Tensor metrico                   |   metric_Mt()       ##
##   T metrico inverso                |   metric_inv_Mt()   ##
##   Simb Christofell clase 1         |   Christofell_Mt(k) ##
##   Simb Christofell Clase 2         |   Conexion_Mt(k)    ##
##   T Riemann 4-Cova                 |   riemann_Mt(i,j)   ##
##   T Riemann 3-Cova y 1-Contrava    |   Riemann_Mt(i,j)   ##
##   T Ricci                          |   Ricci_Mt()        ##
##   Escalar de Curvatura             |   EscalarC()        ##
##                                    |                     ##
##############################################################
##############################################################

class metric:

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
        for i in range(self.n):
            for j in range(self.n):
                if i <= j:
                    self.A.append(self.lista3[i+j][0])
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

        self.g   =   self.A + self.B
        self.G       =    sy.Array(self.g)

    
        #--------------Tensor_metrico _inverso-----------------------#
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

        self.VChristofell  =   []

        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    self.VChristofell.append(christofell(k,j,i)) 

        self.VChristofell  =   sy.Array(self.VChristofell, (self.n, self.n ,self.n))


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

        self.VConexion  =   []

        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    self.VConexion.append(conexion(i,j,k)) 

        self.VConexion  =   sy.Array(self.VConexion, (self.n, self.n, self.n))


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

        self.Vriemann     =   []

        for p in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        self.SS  =   (
                                sy.diff(self.VChristofell[p,i,k], self.var[j]) - 
                                sy.diff(self.VChristofell[p,i,j], self.var[k]) + 
                                DD(p,i,j,k)
                                )

                        self.SS  =   sy.simplify(sy.factor(self.SS))
                        self.Vriemann.append(self.SS)

        self.Vriemann     =   sy.Array(self.Vriemann, (self.n, self.n, self.n, self.n))


        #############################################################
        ##-----Tensor_de_Riemann_3-Covariante_1-Contravariante-----##
        #############################################################


        def TRiemann(p,i,j,k):
            TT  =   0
            for s in range(self.n):
                TT  =   TT + self.Ginv[p,s]*self.Vriemann[s,i,j,k]
                TT  =   sy.simplify(sy.factor(TT))
            return TT

        self.VRiemann     =   []

        for p in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        self.VRiemann.append(TRiemann(p,i,j,k))

        self.VRiemann     =   sy.Array(self.VRiemann, (self.n, self.n, self.n, self.n))


        #############################################################
        ##-------------------Tensor_de_Ricci-----------------------##
        #############################################################

        def ricci(i,j):
            ri  =   0
            for s in range(self.n):
                ri  =   ri + self.VRiemann[s,i,s,j]
                ri  =   sy.simplify(sy.factor(ri))
            return ri

        self.VRicci   =   []

        for i in range(self.n):
            for j in range(self.n):
                self.VRicci.append(ricci(i,j))

        self.VRicci   =   sy.Array(self.VRicci, (self.n, self.n))


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

    def metric_Mt(self):
        return self.G 

    def metric_inv_Mt(self):
        return self.Ginv

    def Christofell_Mt(self,k):
        return self.VChristofell[k]

    def Conexion_Mt(self,k):
        return self.VConexion[k]

    def riemann_Mt(self,j,i): 
        return self.Vriemann[j,i]

    def Riemann_Mt(self,j,i):
        return self.VRiemann[j,i]

    def Ricci_Mt(self):
        return self.VRicci 

    def EscalarC(self):
        return self.VEscalarC


#------------------------------------------------------------#

#--------------------instanciando_objeto---------------------#

os.system("clear")

inst  =   metric("variables.dat","no_variables.dat","tensor_metrico.dat")

print("tensor metrico")
print(inst.metric_Mt(), "\n")

print("tensor metrico inverso")
print(inst.metric_inv_Mt(), "\n")

print("simbolo de chrisfofell")
print(inst.Christofell_Mt(0), "\n")

print("conexion")
print(inst.Conexion_Mt(1), "\n")

print("tensor de riemann")
print(inst.riemann_Mt(0,1), "\n")

print("tensor de Riemann")
print(inst.Riemann_Mt(0,1), "\n")

print("tensor de Ricci")
print(inst.Ricci_Mt(), "\n")

print("Escalar de curvatura")
print(inst.EscalarC())

