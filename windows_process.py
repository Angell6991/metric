import customtkinter as ctk
import threading

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
        self.ventana_calculando.title("Calculando...")
        label = ctk.CTkLabel(self.ventana_calculando, text="Calculando...", fg_color=self.window_bg_color)
        label.pack(pady=20)
        self.ventana_calculando.update()  # Actualizamos la interfaz gráfica manualmente

    def cerrar_ventana_calculando(self):
        if self.ventana_calculando:
            self.ventana_calculando.destroy()
            self.ventana_calculando = None

# Ejemplo de uso:
# app = AppVentanas()
# app.abrir_ventana_calculando()
# print("hola")
# app.cerrar_ventana_calculando()
# print("mundo")
