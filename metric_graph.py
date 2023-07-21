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

from PIL.Image import Image
import PIL as P
import customtkinter as ctk
import os

os.system("clear")

##############################################################
##-------------------Inicio_modo_Visual---------------------##
##############################################################

#---------------configuracion_de_las_ventanas----------------#


#-----------------------colores_y_font-----------------------#

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
font_default    =   ("Inconsolata",15)

#-------------creacion_de_ventana_y_dimenciones--------------#

ventana     =   ctk.CTk()
ventana.geometry("500x600+400+100")
#ventana.overrideredirect(True)
ventana.attributes('-topmost', True)
ventana.wm_attributes('-type', 'splash')

#-------------------------contenido--------------------------#

logo        =   ctk.CTkImage(
        P.Image.open("logo.png"),
        size=(200,180)
        )

log         =   ctk.CTkLabel(ventana,
             image=logo,
             text=""
             )
log.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

name        =   ctk.CTkLabel(
        ventana, 
        text="Metric3", 
        font= ("Z003", 30),
        text_color="#5AEDA3"
        )
name.place(relx=0.5, rely=0.37, anchor=ctk.CENTER)

ctk.CTkLabel(
        ventana, 
        text="Enter the number of:", 
        font=font_default
        ).place(relx=0.5, rely=0.46, anchor=ctk.CENTER)

caja1        =   ctk.CTkEntry(
        ventana, 
        font=font_default, 
        placeholder_text="Dimensions",
        width=165
        )
caja1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

caja2        =   ctk.CTkEntry(
        ventana, 
        font=font_default, 
        placeholder_text="Constants in T.metric",
        width=165
        )
caja2.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

def accion():
    u   = caja1.get()
    return u
 
boton       =   ctk.CTkButton(
        master=ventana, 
        text="Next", 
        font=font_default, 
        command=accion,
        width=70,
        corner_radius=20,
        text_color="#1D1D1D"
        )
boton.place(relx=0.5, rely=0.62, anchor=ctk.CENTER)

ventana.mainloop()

