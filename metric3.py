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
 ##------------------metric_part_3-------------------------##
 ############################################################

from metric2 import*

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



