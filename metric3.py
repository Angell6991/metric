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

import metric as mtc 
import metric2 as mtc2
import pylatex as tex
import sympy as sy
import os 

os.system("clear")

##############################################################
###----------------Parametros_de_entrada-------------------###
##############################################################

###---------------Rutas_archivos_de_texto------------------###

Doc_tex_01  =   "intro_data/variables.dat"
Doc_tex_02  =   "intro_data/no_variables.dat"
Doc_tex_03  =   "intro_data/tensor_metrico.dat"

mtc2.abrir_bloc_de_notas(Doc_tex_01)
mtc2.abrir_bloc_de_notas(Doc_tex_02)
mtc2.abrir_bloc_de_notas(Doc_tex_03)

print("Calculando")

cal =   mtc.metric(Doc_tex_01, Doc_tex_02, Doc_tex_03)
n   =   cal.n

print("Complete \n")


##############################################################
###-------------Construcion_del_document_pdf---------------###
##############################################################

print("Construción del documento pdf")

#-----------Arreglos_para_los_nombres_en_el_pdf--------------#

def chri(i):
    return "\{" + "ij," + str(i) + "\}"

def conex(i):
    return "\\Gamma_{ \: \: ij}" + "^" + str(i)

def rie(i,j):
    return "R_{" + str(i+1) + str(j+1) + "ij}" 

def Rie(i,j):
    return "R^{" + str(i+1) + "}" + "_{ \: \: " + str(j+1) + "ij}" 

#------------Reescritura_de_funciones_a_latex----------------#

latex_metric        =   sy.latex(
        cal.metric_Mt()).replace(
                "\left[","\left( \;").replace(
                        "\\right]","\; \\right)") 

latex_metric_int    =   sy.latex(
        cal.metric_inv_Mt()).replace(
                "\left[","\left( \;").replace(
                        "\\right]","\; \\right)")

latex_chritofell    =   []
for i in range(n):
    latex_chritofell.append(sy.latex(
        cal.Christofell_Mt(i)).replace(
            "\left[","\left( \;").replace(
                "\\right]","\; \\right)"))

latex_conexion      =   []
for i in range(n):
    latex_conexion.append(sy.latex(
        cal.Conexion_Mt(i)).replace(
            "\left[","\left( \;").replace(
                "\\right]","\; \\right)"))

latex_rimann        =   []
lista_rie           =   []
for i in range(n):
    for j in range(n):
        latex_rimann.append(sy.latex(
            cal.riemann_Mt(i,j)).replace(
                "\left[","\left( \;").replace(
                    "\\right]","\; \\right)"))
        lista_rie.append(rie(i,j))

latex_Rimann        =   []
lista_Rie           =   []
for i in range(n):
    for j in range(n):
        latex_Rimann.append(sy.latex(
            cal.Riemann_Mt(i,j)).replace(
                "\left[","\left( \;").replace(
                    "\\right]","\; \\right)"))
        lista_Rie.append(Rie(i,j))

latex_Ricci         =   sy.latex(
        cal.Ricci_Mt()).replace(
                "\left[","\left( \;").replace(
                        "\\right]","\; \\right)")

Latex_Escalar       =   sy.latex(
        cal.EscalarC()).replace(
                "\left[","\left( \;").replace(
                        "\\right]","\; \\right)")


##############################################################
###---------Construcion_y_escritura_en_latex---------------###
##############################################################


#---------------------Encabezado_latex-----------------------#

doc     =   tex.Document()                                    
doc.preamble.append(tex.NoEscape(r"\usepackage[utf8]{inputenc}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{amsmath}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{amsfonts}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{amssymb}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{graphicx}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{txfonts}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{mathrsfs}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{color}"))
doc.preamble.append(tex.NoEscape(r"\usepackage{parskip}"))
doc.preamble.append(tex.NoEscape(r"\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}"))

#-------------Insertando_texto_en_el_documento---------------#

with doc.create(tex.Section("Tensor Metrico y inverso")):
    doc.append(tex.Math(
        data=[tex.NoEscape("g_{ij} = " + latex_metric)]))
    
    doc.append("\n")
    
    doc.append(tex.Math(
        data=[tex.NoEscape("g^{ij} = " + latex_metric_int)]))
    
    doc.append("\n")

with doc.create(tex.Section("Simbolos de Christofell Clase 1")):
    for i in range(n):
        doc.append(tex.Math(
            data=[tex.NoEscape(
                chri(i+1) + "=" + latex_chritofell[i])]))
        doc.append("\n")
 
with doc.create(tex.Section("Simbolos de Christofell Clase 2")):
    for i in range(n):
        doc.append(tex.Math(
            data=[tex.NoEscape(
                conex(i+1) + "=" + latex_conexion[i])]))
        doc.append("\n")
 
with doc.create(tex.Section("Tensor de Riemann 4-Covariante")):
    for i in range(n*n):
        doc.append(tex.Math(
            data=[tex.NoEscape(
                lista_rie[i] + "=" + latex_rimann[i])]))
        doc.append("\n")
 
with doc.create(tex.Section("Tensor de Riemann 3-Covariante 1-Contravariante")):
    for i in range(n*n):
        doc.append(tex.Math(
            data=[tex.NoEscape(
                lista_Rie[i]  + "=" + latex_Rimann[i])]))
        doc.append("\n")

with doc.create(tex.Section("Tensor de Ricci")):
    doc.append(tex.Math(
        data=[tex.NoEscape("R_{ij} = " + latex_Ricci)]))
    
    doc.append("\n")

with doc.create(tex.Section("Escalar de Curvatura")):
    doc.append(tex.Math(
        data=[tex.NoEscape("R = " + Latex_Escalar)]))
    doc.append("\n")

#--------------------Generando_pdf---------------------------#

# os.remove("Metric_doc.pdf")
doc.generate_pdf("Metric_doc", clean_tex=True)                  #True: borra todos los archivos de latex una vez cerado el pdf
os.system("zathura Metric_doc.pdf &")             

print("Complete \n")

#------------------------------------------------------------#


