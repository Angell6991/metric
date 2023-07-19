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

    def metric_Mt(self):
        
        A   =  []
        for i in range(self.n):
            for j in range(self.n):
                if i <= j:
                    A.append(self.lista3[i+j][0])
                elif i > j:
                    A.append(0)

        A   =   sy.Array(A,(self.n,self.n))

        B   =  []
        for i in range(self.n):
            for j in range(self.n):
                if i > j:
                    B.append(A[j,i])
                elif i <= j:
                    B.append(0)
        B   =   sy.Array(B, (self.n,self.n))

        g   =   A + B
        G       =    sy.Array(g)

        return G
    
    #--------------Tensor_metrico _inverso-----------------------#
    def metric_inv_Mt(self):
        Gin  =   sy.simplify(sy.factor(sy.Matrix(self.metric_Mt()).inv()))
        return sy.Array(Gin)


    ##############################################################
    ##----------Simbolos_de_Christofell_Clase_1-----------------##
    ##############################################################

    def Christofell_Mt(self,s):
        G   =   self.metric_Mt()
        var =   self.var

        def christofell(k,j,i):
            ch  =   (
                    sy.diff(G[j,k],var[i]) + 
                    sy.diff(G[i,k],var[j]) - 
                    sy.diff(G[i,j],var[k]) 
                    )/2 
            return ch

        VChristofell  =   []

        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    VChristofell.append(christofell(k,j,i)) 

        VChristofell  =   sy.Array(VChristofell, (self.n, self.n ,self.n))

        return VChristofell[s]


    ##############################################################
    ##-----------Simbolos_de_Christofell_Clase_2----------------##
    ##############################################################

    def Conexion_Mt(self,s):
        
        Ginv            =      self.metric_inv_Mt()

        def conexion(i,j,k):
            cx   =   0
            for p in range(self.n):
                D    =   Ginv[k,p]*self.Christofell_Mt(p)[j,i] 
                cx   =   cx + D
                #cx   =   simplify(factor(cx + D)) 
            return cx

        VConexion  =   []

        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    VConexion.append(conexion(i,j,k)) 

        VConexion  =   sy.Array(VConexion, (self.n, self.n, self.n))


        return VConexion[s]


#---istanciando_objeto---#

os.system("clear")

UU  =   metric("variables.dat","no_variables.dat","tensor_metrico.dat")
print(UU.Conexion_Mt(0))
print(UU.Conexion_Mt(1))

"""

#############################################################
##----------Tensor_de_Riemann_4-Covariante-----------------##
#############################################################

print("Tensor de Riemann 4-Covariante")

def DD(p,i,j,k):
    D   =   0 
    for s in range(n):
        D   =   (
                D + VConexion[s,k,p]*VChristofell[s,i,j] 
                  - VConexion[s,j,p]*VChristofell[s,i,k]
                )
        
        D   =   simplify(factor(D))
    return D

Vriemann     =   []

for p in range(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                SS  =   (
                        diff(VChristofell[p,i,k], var[j]) - 
                        diff(VChristofell[p,i,j], var[k]) + 
                        DD(p,i,j,k)
                        )

                SS  =   simplify(factor(SS))
                Vriemann.append(SS)
              
Vriemann     =   Array(Vriemann, (n,n,n,n))

print("Complete \n")


#############################################################
##-----Tensor_de_Riemann_3-Covariante_1-Contravariante-----##
#############################################################

print("Tensor de Riemann 3-Covariante y 1-Contravariante")

def TRiemann(p,i,j,k):
    TT  =   0
    for s in range(n):
        TT  =   TT + Ginv[p,s]*Vriemann[s,i,j,k]
        TT  =   simplify(factor(TT))
    return TT

VRiemann     =   []

for p in range(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                VRiemann.append(TRiemann(p,i,j,k))

VRiemann     =   Array(VRiemann, (n,n,n,n))

print("Complete \n")


#############################################################
##-------------------Tensor_de_Ricci-----------------------##
#############################################################

print("Tensor de Ricci")

def ricci(i,j):
    ri  =   0
    for s in range(n):
        ri  =   ri + VRiemann[s,i,s,j]
        ri  =   simplify(factor(ri))
    return ri

VRicci   =   []

for i in range(n):
    for j in range(n):
        VRicci.append(ricci(i,j))

VRicci   =   Array(VRicci, (n,n))

print("Complete \n")


#############################################################
##-----------------Escalar_de_Curvatura--------------------##
#############################################################

print("Escalar de Curvatura")

VEscalarC = 0
for i in range(n):
    for j in range(n):
        VEscalarC    =   VEscalarC + Ginv[i,j]*VRicci[i,j]
        VEscalarC    =   simplify(factor(VEscalarC)) 

print("Complete \n")


##############################################################
##--------Definicion_de_funciones_en_forma_matricial--------##
##############################################################



def riemann_Mt(j,i): 
    return Vriemann[j,i]

def Riemann_Mt(j,i):
    return VRiemann[j,i]

def Ricci_Mt():
    return VRicci

def EscalarC():
    return VEscalarC

#------------------------------------------------------------#

"""

