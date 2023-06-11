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


#-----------Arreglos_para_los_nombres_en_el_pdf--------------#

def chri(i):
    return "\{" + "ij," + str(i) + "\}"

def conex(i):
    return "\\Gamma_{ \: \: ij}" + "^" + str(i)

def rie(i,j):
    return "R_{" + str(i+1) + str(j+1) + "ij}" 

def Rie(i,j):
    return "R^{" + str(i+1) + "}" + "_{ \: \: " + str(j+1) + "ij}" 

#----------------Definicion_por_componentes------------------#

# def metric(i,j):
#     return G[i,j] 

# def metric_inv(i,j):
#     return Ginv[i,j]

# def Christofell(k,j,i):
#     return VChristofell[k,j,i]

# def Conexion(k,j,i):
#     return VConexion[k,j,i]

# def riemann(p,k,j,i): 
#     return Vriemann[p,k,j,i]

# def Riemann(p,k,j,i):
#     return VRiemann[p,k,j,i]

# def Ricci(i,j):
#     return VRicci[i,j]

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
doc.preamble.append(NoEscape(r"\usepackage[utf8]{inputenc}"))
doc.preamble.append(NoEscape(r"\usepackage[spanish]{babel}"))
doc.preamble.append(NoEscape(r"\usepackage{amsmath}"))
doc.preamble.append(NoEscape(r"\usepackage{amsfonts}"))
doc.preamble.append(NoEscape(r"\usepackage{amssymb}"))
doc.preamble.append(NoEscape(r"\usepackage{graphicx}"))
doc.preamble.append(NoEscape(r"\usepackage{txfonts}"))
doc.preamble.append(NoEscape(r"\usepackage{mathrsfs}"))
doc.preamble.append(NoEscape(r"\usepackage{color}"))
doc.preamble.append(NoEscape(r"\usepackage{parskip}"))
doc.preamble.append(NoEscape(r"\usepackage[spanish]{babel}"))
doc.preamble.append(NoEscape(r"\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}"))

#------------Reescritura_de_funciones_a_latex----------------#

print("Pasando a latex")

latex_metric        =   latex(metric_Mt()).replace("\left[","\left( \;").replace("\\right]","\; \\right)") 
latex_metric_int    =   latex(metric_inv_Mt()).replace("\left[","\left( \;").replace("\\right]","\; \\right)")

latex_chritofell    =   []
for i in range(n):
    latex_chritofell.append(latex(Christofell_Mt(i)).replace("\left[","\left( \;").replace("\\right]","\; \\right)"))

latex_conexion      =   []
for i in range(n):
    latex_conexion.append(latex(Conexion_Mt(i)).replace("\left[","\left( \;").replace("\\right]","\; \\right)"))

latex_rimann        =   []
lista_rie           =   []
for i in range(n):
    for j in range(n):
        latex_rimann.append(latex(riemann_Mt(i,j)).replace("\left[","\left( \;").replace("\\right]","\; \\right)"))
        lista_rie.append(rie(i,j))

latex_Rimann        =   []
lista_Rie           =   []
for i in range(n):
    for j in range(n):
        latex_Rimann.append(latex(Riemann_Mt(i,j)).replace("\left[","\left( \;").replace("\\right]","\; \\right)"))
        lista_Rie.append(Rie(i,j))

latex_Ricci         =   latex(Ricci_Mt()).replace("\left[","\left( \;").replace("\\right]","\; \\right)")

Latex_Escalar       =   latex(EscalarC()).replace("\left[","\left( \;").replace("\\right]","\; \\right)")

print("Complete \n")

#-------------Insertando_texto_en_el_documento---------------#

print("Construcion del documento pdf")

with doc.create(Section("Tensor Metrico y inverso")):
    doc.append(Math(data=[NoEscape("g_{ij} = " + latex_metric)]))
    doc.append("\n")
    doc.append(Math(data=[NoEscape("g^{ij} = " + latex_metric_int)]))
    doc.append("\n")

with doc.create(Section("Simbolos de Christofell Clase 1")):
    for i in range(n):
        doc.append(Math(data=[NoEscape(chri(i+1) + "=" + latex_chritofell[i])]))
        doc.append("\n")
 
with doc.create(Section("Simbolos de Christofell Clase 2")):
    for i in range(n):
        doc.append(Math(data=[NoEscape(conex(i+1) + "=" + latex_conexion[i])]))
        doc.append("\n")
 
with doc.create(Section("Tensor de Riemann 4-Covariante")):
    for i in range(n*n):
        doc.append(Math(data=[NoEscape(lista_rie[i] + "=" + latex_rimann[i])]))
        doc.append("\n")
 
with doc.create(Section("Tensor de Riemann 3-Covariante 1-Contravariante")):
    for i in range(n*n):
        doc.append(Math(data=[NoEscape(lista_Rie[i]  + "=" + latex_Rimann[i])]))
        doc.append("\n")

with doc.create(Section("Tensor de Ricci")):
    doc.append(Math(data=[NoEscape("R_{ij} = " + latex_Ricci)]))
    doc.append("\n")

with doc.create(Section("Escalar de Curvatura")):
    doc.append(Math(data=[NoEscape("R = " + Latex_Escalar)]))
    doc.append("\n")


#--------------------Generando_pdf---------------------------#

doc.generate_pdf("Metric_doc", clean_tex=True)                  #True: borra todos los archivos de latex una vez cerado el pdf
os.system("zathura Metric_doc.pdf &")

print("Complete \n")

#------------------------------------------------------------#



