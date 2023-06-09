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
#   Tensor metrico                      metric(i,j)          #
#   T metrico inverso                   metric_inv(i,j)      #
#   Simb Christofell clase 1            Christofell(k,j,i)   #
#   Simb Christofell Clase 2            Conexion(k,j,i)      #
#   T Riemann 4-Cova                    riemann(p,k,j,i)     #
#   T Riemann 3-Cova y 1-Contrava       Riemann(p,k,j,i)     #
#   T Ricci                             Ricci(i,j)           #
#   Escalar de Curvatura                EscalarC             #
#                                                            #
##############################################################

##############################################################
##-----------------Parametros_de_entrada--------------------##
##############################################################


#------------------Variables_simbolicas----------------------#

var     =    ["psi", "theta", "phi"]                                                                            #insert variables
r       =    symbols("r")
var     =    symbols(var)
n       =    len(var)

#---------------Tensor_Metrico_y_inverso---------------------#

g       =    [[(r**2),0,0],[0,(r**2)*(sin(var[0])**2),0],[0,0,(r**2)*(sin(var[0])**2)*(sin(var[1])**2)]]        #inset T metric
G       =    Array(g)
Ginv    =    simplify(factor(Array(Matrix(g).inv())))

#------------------------------------------------------------#



