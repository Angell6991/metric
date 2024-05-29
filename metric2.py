import tkinter as tk
from tkinter import scrolledtext

class BlocDeNotas:
    def __init__(self, archivo_predeterminado):
        self.root = tk.Tk()
        self.archivo_predeterminado = archivo_predeterminado
        
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(expand=True, fill="both")
        
        with open(archivo_predeterminado, 'r') as archivo:
            contenido = archivo.read()
            self.text_area.insert(tk.END, contenido)
        
        self.nombre_archivo_label = tk.Label(self.root, text=archivo_predeterminado)
        self.nombre_archivo_label.pack(side=tk.TOP, fill=tk.X)
        
        self.guardar_y_cerrar = tk.Button(self.root, text="Next", command=self.guardar_y_cerrar)
        self.guardar_y_cerrar.pack()

    def guardar_y_cerrar(self):
        contenido = self.text_area.get("1.0", tk.END)
        with open(self.archivo_predeterminado, 'w') as archivo:
            archivo.write(contenido)
        self.root.destroy()

def abrir_bloc_de_notas(archivo):
    app = BlocDeNotas(archivo)
    app.root.mainloop()

# if __name__ == "__main__":
#     abrir_bloc_de_notas("variables.dat")

