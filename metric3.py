import modules.metric_construc_pdf as cpdf  
import modules.metric_block_note as block
import modules.metric_windows as ws
import os

##################################################
###--------Introcciendo_ruta_de_data-----------###
##################################################

# ruta    =   os.getcwd() #obtener la ruta del directorio con python, esto es equibalente al comado "pwd"
ruta_usuario    =   os.path.expanduser("~/") #muestra la ruta de usuario, equibalente a pwd en directorio ~/ 

doc_texto_01  =   ruta_usuario + "/.config/metric/support_files/intro_data/variables.dat"
doc_texto_02  =   ruta_usuario + "/.config/metric/support_files/intro_data/no_variables.dat"
doc_texto_03  =   ruta_usuario + "/.config/metric/support_files/intro_data/tensor_metrico.dat"

###----Editando_data_con_el_block_de_notas-----###

block.abrir_bloc_de_notas(doc_texto_01)
block.abrir_bloc_de_notas(doc_texto_02)
block.abrir_bloc_de_notas(doc_texto_03)

##################################################
###--------ventana_de_carga_y_view_pdf---------###
##################################################

# La funcion vantana_carga muestra la ventana de carga
# mientrans la funcion construc_pdf construye el pdf
# dentro de la funcion ventana_carga se utiliza lambda:
# para que al pasarle la funcion construc_pdf esta se 
# exporte con todos sus parametro y no halla errores

ws.ventana_carga(
        lambda: cpdf.construc_pdf(doc_texto_01,doc_texto_02,doc_texto_03))

###------------------view_pdf------------------###
ws.ventana_finalizada("zathura " + ruta_usuario + "/Metric_doc.pdf &")

