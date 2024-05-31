import customtkinter as ctk
import threading
import os

class AppVentanas:
    def __init__(self, window_bg_color="#1D1D1D", font_color="#FFFFFF", button_bg_color="#5AEDA3"):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.window_bg_color = window_bg_color
        self.font_color = font_color
        self.button_bg_color = button_bg_color

        self.ventana_calculando = None

    def abrir_ventana_calculando(self):
        self.ventana_calculando = ctk.CTk()
        self.ventana_calculando.geometry("200x100")
        self.ventana_calculando.configure(fg_color=self.window_bg_color)
        # self.ventana_calculando.title("Calculando...")
        label = ctk.CTkLabel(self.ventana_calculando, text="Calculated.....", fg_color=self.window_bg_color)
        label.pack(pady=20)
        self.ventana_calculando.update()  # Actualizamos la interfaz gráfica manualmente

    def cerrar_ventana_calculando(self):
        if self.ventana_calculando:
            self.ventana_calculando.destroy()
            self.ventana_calculando = None


def ventana_finalizada(accion_terminal, 
                       font_family="Inconsolata", 
                       font_size=20, font_color="#FFFFFF", 
                       window_bg_color="#1D1D1D", 
                       button_bg_color="#5AEDA3"):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("300x150")  # Define el tamaño de la ventana
    root.configure(fg_color=window_bg_color)

    mensaje_label = ctk.CTkLabel(
        root, 
        text="Calculation complete", 
        fg_color=window_bg_color, 
        text_color=font_color,
        font=(font_family, 20))
    mensaje_label.pack(side=ctk.TOP, pady=(40, 10))

    def ejecutar_accion():
        os.system(accion_terminal)  # Ejecuta la acción en la terminal
        root.destroy()  # Cierra la ventana

    boton = ctk.CTkButton(
        root, 
        text="View PDF", 
        command=ejecutar_accion, 
        fg_color=button_bg_color,
        text_color=window_bg_color,
        hover_color="#FFFFFF",
        font=(font_family, font_size))  
    boton.pack(pady=(10, 20))

    root.mainloop()


####################################################
###--------------------Prueva--------------------###
####################################################

# ventana_finalizada("echo 'Hola, mundo'")
# Ejemplo de uso:
# app = AppVentanas()
# app.abrir_ventana_calculando()
# print("hola")
# app.cerrar_ventana_calculando()
# print("mundo")
