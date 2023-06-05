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
#------------------Parametros_de_entrada---------------------#
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
#----------------Definicion_de_funciones---------------------#
##############################################################


#-----------Simbolos_de_Christofell_Clase_1------------------#

def christofell(i,j,k):
    ch  =   simplify(factor( ( diff(G[j,k],var[i]) + diff(G[i,k],var[j]) - diff(G[i,j],var[k]) )/2 ))
    return ch

#-----------Simbolos_de_Christofell_Clase_2------------------#

def conexion(k,j,i):
    cx   =   0
    for s in range(n):
        D    =   Ginv[k,s]*christofell(i,j,s) 
        cx   =   simplify(factor(cx + D)) 
    return cx

#-----------Tensor_de_Riemann_4-Covariante------------------#

def riemann(p,i,j,k):

    DD = [0]*n 
    for u in range(n):
        DD[u]   =   [0]*n    

    DDD = [0]*n 
    for u in range(n):
        DDD[u]   =   [0]*n 

    for u1 in range(n):
        for u2 in range(n):
            DD[u1][u2] = DDD

    for s in range(n):
        DD[p][i][j][k]  =   factor(DD[p][i][j][k] + conexion(s,k,p)*christofell(i,j,s) - conexion(s,j,p)*christofell(i,k,s))

    riem    =   factor(diff(christofell(i,k,p), var[j]) - diff(christofell(i,j,p), var[k]) + DD[p][i][j][k])
    riem    =   simplify(riem)
    return riem

#------Tensor_de_Riemann_3-Covariante_1-Contravariante------#

def TRiemann(p,i,j,k):
    TR      =   0
    for s in range(n):
        TR  =   TR + Ginv[p,s]*riemann(s,i,j,k)
        TR  =   simplify(factor(TR))
    return TR

#--------------------Tensor_de_Ricci------------------------#

def ricci(i,j):
    ric    =   0
    for s in range(n):
        ric    =   ric + TRiemann(s,i,s,j)
        ric    =   simplify(factor(ric))
    return ric

#------------------Escalar_de_Curvatura---------------------#

def Rcurva():
    curv    =   0
    for i in range(n):
        for j in range(n):
            curv    =   curv + Ginv[i,j]*ricci(i,j)
            curv    =   simplify(factor(curv))
    return curv


##############################################################
#---------------Visualizacion_de_resultados------------------#
##############################################################



