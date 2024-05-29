import tkinter as tk
from tkinter import scrolledtext
from tkinter import colorchooser
from PIL import Image, ImageTk  # Importar Pillow

class BlocDeNotas:
    default_image_path = "logo_doc/logo.png"
    
    def __init__(self, archivo_predeterminado, font_color="#FFFFFF", window_bg_color="#1D1D1D", text_bg_color="#353535", button_bg_color="#5AEDA3"):
        self.root = tk.Tk()
        self.root.configure(bg=window_bg_color)
        self.archivo_predeterminado = archivo_predeterminado
        self.font_color = font_color
        self.window_bg_color = window_bg_color
        self.text_bg_color = text_bg_color
        self.button_bg_color = button_bg_color
        
        self.imagen = Image.open(self.default_image_path)
        self.imagen.thumbnail((180, 150))  # Redimensionar la imagen manteniendo la proporción
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        
        self.imagen_label = tk.Label(self.root, image=self.imagen_tk, bg=self.window_bg_color)
        self.imagen_label.pack(side=tk.TOP)
        
        self.scrollbar_x = tk.Scrollbar(self.root, orient="horizontal")
        
        self.text_area = scrolledtext.ScrolledText(self.root, wrap="none", width=50, height=20, xscrollcommand=self.scrollbar_x.set)
        self.text_area.pack(expand=True, fill="both")
        self.text_area.configure(fg=self.font_color, bg=self.text_bg_color)
        
        self.scrollbar_x.config(command=self.text_area.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        
        with open(archivo_predeterminado, 'r') as archivo:
            contenido = archivo.read()
            self.text_area.insert(tk.END, contenido)
        
        self.nombre_archivo_label = tk.Label(self.root, text=archivo_predeterminado, bg=self.window_bg_color, fg=self.font_color)
        self.nombre_archivo_label.pack(side=tk.TOP, fill=tk.X)
        
        self.guardar_y_cerrar = tk.Button(self.root, text="Next", command=self.guardar_y_cerrar, bg=self.button_bg_color)
        self.guardar_y_cerrar.pack()

    def guardar_y_cerrar(self):
        contenido = self.text_area.get("1.0", tk.END)
        with open(self.archivo_predeterminado, 'w') as archivo:
            archivo.write(contenido)
        self.root.destroy()

def abrir_bloc_de_notas(archivo):
    app = BlocDeNotas(archivo)
    app.root.mainloop()


if __name__ == "__main__":
    abrir_bloc_de_notas("intro_data/variables.dat")

