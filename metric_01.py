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

#------------------Variables_simbolicas----------------------#

var     =    ["r", "phi", "theta"]
var     =    symbols(var)
n       =    len(var)

#---------------Tensor_Metrico_y_inverso---------------------#

g       =    [[1,0,0],[0,(var[0]**2)*(sin(var[2])**2),0],[0,0,var[0]**2]]
G       =    Array(g)
Ginv    =    simplify(Array(Matrix(g).inv()))

#-----------Simbolos_de_Christofell_Clase_1------------------#

def christofell(i,j,k):
    ch  =   simplify( (1/2)*( diff(G[j,k],var[i]) + diff(G[i,k],var[j]) - diff(G[i,j],var[k]) ) )
    return ch

print(christofell(0,1,1))
