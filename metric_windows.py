import customtkinter as ctk
import threading
import os


####################################################
###----------------Loading_window----------------###
####################################################

def ventana_carga(proceso, 
                  font_family="Inconsolata", 
                  font_size=20, font_color="#FFFFFF", 
                  window_bg_color="#1D1D1D", 
                  loading_text="Calculated....."):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("300x150")  # Define el tamaño de la ventana
    root.configure(fg_color=window_bg_color)

    mensaje_label = ctk.CTkLabel(
        root, 
        text=loading_text, 
        fg_color=window_bg_color, 
        text_color=font_color,
        font=(font_family, font_size))
    mensaje_label.pack(side=ctk.TOP, pady=(40, 10))

    def ejecutar_proceso():
        proceso()  # Ejecuta el proceso proporcionado
        root.destroy()  # Cierra la ventana de carga una vez que el proceso termina

    # Inicia el proceso en un hilo separado para no bloquear la interfaz gráfica
    hilo_proceso = threading.Thread(target=ejecutar_proceso)
    hilo_proceso.start()

    root.mainloop()


####################################################
###---------------Window_view_PDF----------------###
####################################################

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

#def ejemplo_calculo():
#    import time
#    time.sleep(5)  # Simula un cálculo que toma 5 segundos

##se usa lambda para resivir la funcion con todo susargumentos
#ventana_carga(lambda: ejemplo_calculo)

#ventana_finalizada("echo 'Hola, mundo'")

