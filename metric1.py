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



