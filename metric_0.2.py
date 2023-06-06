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

from sympy import*
import os

os.system("clear")

##############################################################
#--------------------Guia_de_funciones-----------------------#
#                                                            #
#   Tensor metrico                      G[i,j]               #
#   T metrico inverso                   Ginv[i,j]            #
#   Simb Christofell clase 1            Christofell[k,j,i]   #
#   Simb Christofell Clase 2            Conexion[k,j,i]      #
#   T Riemann 4-Cova                    riemann[p,k,j,i]     #
#   T Riemann 3-Cova y 1-Contrava       Riemann[p,k,j,i]     #
#   T Ricci                             Ricci[i,j]           #
#   Escalar de Curvatura                EscalarC             #
#                                                            #
##############################################################

##############################################################
##-----------------Parametros_de_entrada--------------------##
##############################################################


#------------------Variables_simbolicas----------------------#

var     =    ["psi", "theta", "phi"]
r       =    symbols("r")
var     =    symbols(var)
n       =    len(var)

#---------------Tensor_Metrico_y_inverso---------------------#

g       =    [[(r**2),0,0],[0,(r**2)*(sin(var[0])**2),0],[0,0,(r**2)*(sin(var[0])**2)*(sin(var[1])**2)]]
G       =    Array(g)
Ginv    =    simplify(factor(Array(Matrix(g).inv())))


##############################################################
##----------Simbolos_de_Christofell_Clase_1-----------------##
##############################################################

def christofell(k,j,i):
    ch  =   (
             diff(G[j,k],var[i]) + 
             diff(G[i,k],var[j]) - 
             diff(G[i,j],var[k]) 
             )/2 
    
    ch  =   simplify(factor(ch))
    return ch

#------------------------Visual------------------------------#

print("Simbolos de Christofell Clase 1")

Christofell  =   []

for k in range(n):
    for j in range(n):
        for i in range(n):
            Christofell.append(christofell(k,j,i)) 

Christofell  =   Array(Christofell, (n,n,n))

print("Complete \n")


##############################################################
##-----------Simbolos_de_Christofell_Clase_2----------------##
##############################################################

def conexion(i,j,k):
    cx   =   0
    for s in range(n):
        D    =   Ginv[k,s]*Christofell[s,j,i] 
        cx   =   simplify(factor(cx + D)) 
    return cx

#------------------------Visual------------------------------#

print("Simbolos de Christofell Clase 2")

Conexion  =   []

for k in range(n):
    for j in range(n):
        for i in range(n):
            Conexion.append(conexion(i,j,k)) 

Conexion  =   Array(Conexion, (n,n,n))

print("Complete \n")


#############################################################
##----------Tensor_de_Riemann_4-Covariante-----------------##
#############################################################

print("Tensor de Riemann 4-Covariante")

def DD(p,i,j,k):
    D   =   0 
    for s in range(n):
        D   =   (
                D + Conexion[s,k,p]*Christofell[s,i,j] 
                  - Conexion[s,j,p]*Christofell[s,i,k]
                )
        
        D   =   simplify(factor(D))
    return D

riemann     =   []

for p in range(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                SS  =   (
                        diff(Christofell[p,i,k], var[j]) - 
                        diff(Christofell[p,i,j], var[k]) + 
                        DD(p,i,j,k)
                        )

                SS  =   simplify(factor(SS))
                riemann.append(SS)
              
riemann     =   Array(riemann, (n,n,n,n))

print("Complete \n")


#############################################################
##-----Tensor_de_Riemann_3-Covariante_1-Contravariante-----##
#############################################################

print("Tensor de Riemann 3-Covariante y 1-Contravariante")

def TRiemann(p,i,j,k):
    TT  =   0
    for s in range(n):
        TT  =   TT + Ginv[p,s]*riemann[s,i,j,k]
        TT  =   simplify(factor(TT))
    return TT

Riemann     =   []

for p in range(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Riemann.append(TRiemann(p,i,j,k))

Riemann     =   Array(Riemann, (n,n,n,n))

print("Complete \n")


#############################################################
##-------------------Tensor_de_Ricci-----------------------##
#############################################################

print("Tensor de Ricci")

def ricci(i,j):
    ri  =   0
    for s in range(n):
        ri  =   ri + Riemann[s,i,s,j]
        ri  =   simplify(factor(ri))
    return ri

Ricci   =   []

for i in range(n):
    for j in range(n):
        Ricci.append(ricci(i,j))

Ricci   =   Array(Ricci, (n,n))

print("Complete \n")


#############################################################
##-----------------Escalar_de_Curvatura--------------------##
#############################################################

print("Escalar de Curvatura")

EscalarC = 0
for i in range(n):
    for j in range(n):
        EscalarC    =   EscalarC + Ginv[i,j]*Ricci[i,j]
        EscalarC    =   simplify(factor(EscalarC)) 

print("Complete \n")


##############################################################
#---------------Visualizacion_de_resultados------------------#
##############################################################



