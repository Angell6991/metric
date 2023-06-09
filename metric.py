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

VChristofell  =   []

for k in range(n):
    for j in range(n):
        for i in range(n):
            VChristofell.append(christofell(k,j,i)) 

VChristofell  =   Array(VChristofell, (n,n,n))

print("Complete \n")


##############################################################
##-----------Simbolos_de_Christofell_Clase_2----------------##
##############################################################

def conexion(i,j,k):
    cx   =   0
    for s in range(n):
        D    =   Ginv[k,s]*VChristofell[s,j,i] 
        cx   =   simplify(factor(cx + D)) 
    return cx

#------------------------Visual------------------------------#

print("Simbolos de Christofell Clase 2")

VConexion  =   []

for k in range(n):
    for j in range(n):
        for i in range(n):
            VConexion.append(conexion(i,j,k)) 

VConexion  =   Array(VConexion, (n,n,n))

print("Complete \n")


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
##--------------Visualizacion_de_resultados-----------------##
##############################################################


#----------------Definicion_por_componentes------------------#

def metric(i,j):
    return G[i,j] 

def metric_inv(i,j):
    return Ginv[i,j]

def Christofell(k,j,i):
    return VChristofell[k,j,i]

def Conexion(k,j,i):
    return VConexion[k,j,i]

def riemann(p,k,j,i): 
    return Vriemann[p,k,j,i]

def Riemann(p,k,j,i):
    return VRiemann[p,k,j,i]

def Ricci(i,j):
    return VRicci[i,j]

def EscalarC():
    return VEscalarC

#------------------Definicion_por_Matrices-------------------#

def metric_Mt():
    return G 

def metric_inv_Mt():
    return Ginv

def Christofell_Mt(k):
    return VChristofell[k]

def Conexion_Mt(k):
    return VConexion[k]

def riemann_Mt(j,i): 
    return Vriemann[j,i]

def Riemann_Mt(j,i):
    return VRiemann[j,i]

def Ricci_Mt():
    return VRicci


##############################################################
##--------------Construcion_del_document_pdf----------------##
##############################################################

doc     =   Document()

#------------Reescritura_de_funciones_a_latex----------------#

print("Pasando a latex")

latex_metric        =   latex(metric_Mt()) 
latex_metric_int    =   latex(metric_inv_Mt())

latex_chritofell    =   []
for i in range(n):
    latex_chritofell.append(latex(Christofell_Mt(i)))

latex_conexion      =   []
for i in range(n):
    latex_conexion.append(latex(Conexion_Mt(i)))

latex_rimann        =   []
for i in range(n):
    for j in range(n):
        latex_rimann.append(latex(riemann_Mt(i,j)))

latex_Rimann        =   []
for i in range(n):
    for j in range(n):
        latex_Rimann.append(latex(Riemann_Mt(i,j)))

latex_Ricci         =   latex(Ricci_Mt())

Latex_Escalar       =   latex(EscalarC())

print("Complete \n")

#-------------Insertando_texto_en_el_documento---------------#

print("Construcion del documento pdf")

with doc.create(Section("Tensor Metrico y inverso")):
    doc.append(Math(data=[NoEscape("g_{ij} = " + latex_metric)]))
    doc.append(Math(data=[NoEscape("g^{ij} = " + latex_metric_int)]))

with doc.create(Section("Simbolos de Christofell Clase 1")):
    for i in range(n):
        doc.append(Math(data=[NoEscape(latex_chritofell[i])]))

with doc.create(Section("Simbolos de Christofell Clase 2")):
    for i in range(n):
        doc.append(Math(data=[NoEscape(latex_conexion[i])]))

with doc.create(Section("Tensor de Riemann 4-Covariante")):
    for i in range(n*n):
        doc.append(Math(data=[NoEscape(latex_rimann[i])]))

with doc.create(Section("Tensor de Riemann 3-Covariante 1-Contravariante")):
    for i in range(n*n):
        doc.append(Math(data=[NoEscape(latex_Rimann[i])]))

with doc.create(Section("Tensor de Ricci")):
    doc.append(Math(data=[NoEscape(latex_Ricci)]))

with doc.create(Section("Escalar de Curvatura")):
    doc.append(Math(data=[NoEscape(Latex_Escalar)]))

print("Complete \n")

#--------------------Generando_pdf---------------------------#

doc.generate_pdf("Metric_doc", clean_tex=True)                  #True: borra todos los archivos de latex una vez cerado el pdf
os.system("zathura Metric_doc.pdf &")

#------------------------------------------------------------#


