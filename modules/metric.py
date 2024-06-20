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

        self.VChristofell  =   []

        for k in range(self.n):
            for j in range(self.n):
                for i in range(self.n):
                    self.VChristofell.append(christofell(k,j,i)) 

        self.VChristofell  =   sy.Array(self.VChristofell, (self.n, self.n ,self.n))


        ##############################################################
        ##-----------Simbolos_de_Christofell_Clase_2----------------##
        ##############################################################

        #def conexion(i,j,k):
        #    cx   =   0
        #    for p in range(self.n):
        #        D    =   self.Ginv[k,p]*self.VChristofell[p,j,i] 
        #        cx   =   cx + D
        #        #cx   =   simplify(factor(cx + D)) 
        #    return cx

        #self.VConexion  =   []

        #for k in range(self.n):
        #    for j in range(self.n):
        #        for i in range(self.n):
        #            self.VConexion.append(conexion(i,j,k)) 

        #self.VConexion  =   sy.Array(self.VConexion, (self.n, self.n, self.n))


        #############################################################
        ##----------Tensor_de_Riemann_4-Covariante-----------------##
        #############################################################

        # def DD(p,i,j,k):
        #     D   =   0 
        #     for s in range(self.n):
        #         D   =   (
        #                 D + self.VConexion[s,k,p]*self.VChristofell[s,i,j] 
        #                 - self.VConexion[s,j,p]*self.VChristofell[s,i,k]
        #                 )

        #         D   =   sy.simplify(sy.factor(D))
        #     return D

        # self.Vriemann     =   []

        # for p in range(self.n):
        #     for i in range(self.n):
        #         for j in range(self.n):
        #             for k in range(self.n):
        #                 self.SS  =   (
        #                         sy.diff(self.VChristofell[p,i,k], self.var[j]) - 
        #                         sy.diff(self.VChristofell[p,i,j], self.var[k]) + 
        #                         DD(p,i,j,k)
        #                         )

        #                 self.SS  =   sy.simplify(sy.factor(self.SS))
        #                 self.Vriemann.append(self.SS)

        # self.Vriemann     =   sy.Array(self.Vriemann, (self.n, self.n, self.n, self.n))


        #############################################################
        ##-----Tensor_de_Riemann_3-Covariante_1-Contravariante-----##
        #############################################################


        # def TRiemann(p,i,j,k):
        #     TT  =   0
        #     for s in range(self.n):
        #         TT  =   TT + self.Ginv[p,s]*self.Vriemann[s,i,j,k]
        #         TT  =   sy.simplify(sy.factor(TT))
        #     return TT

        # self.VRiemann     =   []

        # for p in range(self.n):
        #     for i in range(self.n):
        #         for j in range(self.n):
        #             for k in range(self.n):
        #                 self.VRiemann.append(TRiemann(p,i,j,k))

        # self.VRiemann     =   sy.Array(self.VRiemann, (self.n, self.n, self.n, self.n))


        #############################################################
        ##-------------------Tensor_de_Ricci-----------------------##
        #############################################################

        # def ricci(i,j):
        #     ri  =   0
        #     for s in range(self.n):
        #         ri  =   ri + self.VRiemann[s,i,s,j]
        #         ri  =   sy.simplify(sy.factor(ri))
        #     return ri

        # self.VRicci   =   []

        # for i in range(self.n):
        #     for j in range(self.n):
        #         self.VRicci.append(ricci(i,j))

        # self.VRicci   =   sy.Array(self.VRicci, (self.n, self.n))


        #############################################################
        ##-----------------Escalar_de_Curvatura--------------------##
        #############################################################

        # self.VEscalarC = 0
        # for i in range(self.n):
        #     for j in range(self.n):
        #         self.VEscalarC    =   self.VEscalarC + self.Ginv[i,j]*self.VRicci[i,j]
        #         self.VEscalarC    =   sy.simplify(sy.factor(self.VEscalarC)) 


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

    # def riemann(self,j,i): 
    #     return self.Vriemann[j,i]

    # def Riemann(self,j,i):
    #     return self.VRiemann[j,i]

    # def Ricci(self):
    #     return self.VRicci 

    # def EscalarC(self):
    #     return self.VEscalarC


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

# print("conexion")
# print(inst.Conexion(1), "\n")

# print("tensor de riemann")
# print(inst.riemann(0,1), "\n")

# print("tensor de Riemann")
# print(inst.Riemann(0,1), "\n")

# print("tensor de Ricci")
# print(inst.Ricci(), "\n")

# print("Escalar de curvatura")
# print(inst.EscalarC())


end_time = time.time()                      # fin del calculo, toma tiempo final 

elapsed_time = end_time - start_time        # Tiempo que tarda en hacer los calculos  
print(f"El tiempo de ejecución fue: {elapsed_time} segundos")

###############################
## time calculation 3-sphera ##
###############################

# simbolo de chrisfofell:   1.8649024963378906s     1.8785393238067627s     1.8800923824310303s     1.918670654296875s
# conexion:                 1.9145839214324951s     1.9280104637145996s     1.9283218383789062s     1.960606336593628s 
# tensor de riemann:        18.94029927253723s      19.243494033813477s     19.2705078125s          19.29889440536499s 
# tensor de Riemann:        20.05891513824463s      20.125524759292603s     20.320835828781128s     20.45212745666504s
# tensor de ricci:          20.36686658859253s      20.518545866012573s     20.779770135879517s     20.92125701904297s
# escalar de curvatura:     20.576985836029053s     20.58171558380127s      20.622387647628784s     21.241875171661377s






