import metric_construc_pdf as cpdf  
import metric_block_note as block
import metric_windows as ws

doc_texto_01  =   "intro_data/variables.dat"
doc_texto_02  =   "intro_data/no_variables.dat"
doc_texto_03  =   "intro_data/tensor_metrico.dat"

block.abrir_bloc_de_notas(doc_texto_01)
block.abrir_bloc_de_notas(doc_texto_02)
block.abrir_bloc_de_notas(doc_texto_03)

ws.ventana_carga(
        lambda: cpdf.construc_pdf(doc_texto_01,doc_texto_02,doc_texto_03))

ws.ventana_finalizada("zathura  Metric_doc.pdf &")

