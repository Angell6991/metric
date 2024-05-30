import customtkinter as ctk
from PIL import Image
import os

#####################################################
####---------------Fonts_necesarias---------------###
#####################################################
####     Tex Gyre Chorus                          ###
####     Inconsolata                              ###
#####################################################


class BlocDeNotas:
    default_image_path = "logo_doc/logo.png"

    def __init__(
            self, 
            archivo_predeterminado, 
            width=400, 
            height=600, 
            font_color="#FFFFFF", 
            window_bg_color="#1D1D1D", 
            text_bg_color="#353535", 
            button_bg_color="#5AEDA3",
            color_puntero="#FFFFFF",
            font_family="Inconsolata",  
            font_size=20):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.geometry(f"{width}x{height}")  # Define el tamaño de la ventana
        self.root.configure(fg_color=window_bg_color)
        self.archivo_predeterminado = archivo_predeterminado
        self.font_color = font_color
        self.window_bg_color = window_bg_color
        self.text_bg_color = text_bg_color
        self.button_bg_color = button_bg_color
        self.color_puntero = color_puntero
        self.font_family = font_family
        self.font_size = font_size

        self._setup_ui()
        self._load_file_content()

    def _setup_ui(self):
        self._setup_image()
        self._setup_labels()
        self._setup_text_area()
        self._setup_save_button()

    def _setup_image(self):
        self.imagen = Image.open(self.default_image_path)
        self.imagen.thumbnail((180, 150))  
        self.imagen_ctk = ctk.CTkImage(self.imagen, size=(180, 150))  
        self.imagen_label = ctk.CTkLabel(
                self.root, text="", image=self.imagen_ctk, fg_color=self.window_bg_color)
        self.imagen_label.pack(side=ctk.TOP, pady=(10, 5))

    def _setup_labels(self):
        self.mensaje_label = ctk.CTkLabel(
            self.root, 
            text="Metric3", 
            fg_color=self.window_bg_color, 
            text_color=self.button_bg_color,
            font=("Tex Gyre Chorus", 40))
        self.mensaje_label.pack(side=ctk.TOP, pady=(0, 10))

        nombre_archivo = os.path.basename(self.archivo_predeterminado)
        nombre_archivo_sin_extension = os.path.splitext(nombre_archivo)[0]

        self.nombre_archivo_label = ctk.CTkLabel(
            self.root, 
            text=f"Introduce {nombre_archivo_sin_extension}",
            fg_color=self.window_bg_color, 
            text_color=self.font_color,
            font=(self.font_family, self.font_size))
        self.nombre_archivo_label.pack(side=ctk.TOP, fill=ctk.X, pady=(0, 10))

    def _setup_text_area(self):
        self.text_area = ctk.CTkTextbox(
            self.root, 
            wrap="none", 
            width=40, 
            height=15, 
            font=(self.font_family, self.font_size)) 
        self.text_area.pack(expand=True, fill="both", padx=20, pady=(0, 10))
        self.text_area.configure(
            text_color=self.font_color, 
            bg_color=self.text_bg_color)

    def _setup_save_button(self):
        self.guardar_y_cerrar_button = ctk.CTkButton(
            self.root, 
            text="Next", 
            command=self.guardar_y_cerrar, 
            fg_color=self.button_bg_color,
            text_color=self.window_bg_color,
            hover_color="#FFFFFF",  
            font=(self.font_family, self.font_size))  
        self.guardar_y_cerrar_button.pack(pady=(10, 20))

    def _load_file_content(self):
        with open(self.archivo_predeterminado, 'r') as archivo:
            contenido = archivo.read()
            self.text_area.insert(ctk.END, contenido)

    def guardar_y_cerrar(self):
        contenido = self.text_area.get("1.0", ctk.END)
        with open(self.archivo_predeterminado, 'w') as archivo:
            archivo.write(contenido)
        self.root.destroy()

def abrir_bloc_de_notas(archivo):
    app = BlocDeNotas(archivo)
    app.root.mainloop()


#####################################################
####-------------------Prueba---------------------###
#####################################################

# abrir_bloc_de_notas("intro_data/no_variables.dat")


