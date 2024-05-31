import metric_window_finish as wf
import metric_construc_pdf as cpdf  
import metric_block_note as block

Doc_texto_01  =   "intro_data/variables.dat"
Doc_texto_02  =   "intro_data/no_variables.dat"
Doc_texto_03  =   "intro_data/tensor_metrico.dat"

block.abrir_bloc_de_notas(Doc_texto_01)
block.abrir_bloc_de_notas(Doc_texto_02)
block.abrir_bloc_de_notas(Doc_texto_03)

print("calculando")
cpdf.construc_pdf(Doc_texto_01,Doc_texto_02,Doc_texto_03)
print("calculo finalizado")

wf.ventana_finalizada("zathura  Metric_doc.pdf &")


