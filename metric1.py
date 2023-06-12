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
 ##------------------metric_part_1-------------------------##
 ############################################################

from sympy import*
from pylatex import Document, Section, Subsection, Command, Math
from pylatex.utils import italic, NoEscape
import os

os.system("clear")

##############################################################
#--------------------Guia_de_funciones-----------------------#
#                                                            #
#   Tensor metrico                      metric_Mt()          #
#   T metrico inverso                   metric_inv_Mt()      #
#   Simb Christofell clase 1            Christofell_Mt(k)    #
#   Simb Christofell Clase 2            Conexion_Mt(k)       #
#   T Riemann 4-Cova                    riemann_Mt(i,j)      #
#   T Riemann 3-Cova y 1-Contrava       Riemann_Mt(i,j)      #
#   T Ricci                             Ricci_Mt()           #
#   Escalar de Curvatura                EscalarC()           #
#                                                            #
##############################################################

##############################################################
##-----------------Parametros_de_entrada--------------------##
##############################################################


##############################################################
##-----------------Variables_simbolicas---------------------##
##############################################################

#---------------------Insert_variables-----------------------#

n       =   int(input("Ingrese el numero de dimenciones: "))
var     =    []                                             
for i in range(n):
        var.append(str(input(f"Variable {i+1}: ")))
var     =    symbols(var)
print()

#-------------------variables_adicionales--------------------#
ss      = "¿cuantos valores constantes posee el tensor metrico? : "
NN       = int(input(ss))
varr     =   []      
for i in range(NN):
    varr.append(str(input(f"Constante {i+1}: ")))
varr    =    symbols(varr)
print()


##############################################################
##--------------Tensor_Metrico_y_inverso--------------------##
##############################################################

#--------------------Tensor_metrico--------------------------#

A   =  []
B   =  []

print("introduce el tensor metrico:")
for i in range(n):
    for j in range(n):
        if i <= j: 
            A.append(input(f"Introduc G{i+1}{j+1}: "))
        elif i > j: 
            A.append(0)
A   =   Array(A, (n,n))

for i in range(n):
    for j in range(n):
        if i > j:
            B.append(A[j,i])
        elif i <= j:
            B.append(0)
B   =   Array(B, (n,n))

g   =   A + B
G       =    Array(g)

#--------------Tensor_metrico _inverso-----------------------#

Ginv    =    simplify(factor(Array(Matrix(g).inv())))

os.system("clear")

#------------------------------------------------------------#



