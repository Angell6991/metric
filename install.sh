#!/bin/bash

echo "Instalando dependencias..."
sudo dnf install -y python python-pip zathura python-tkinter
clear

echo "Instalando librerías de Python..."
pip install sympy pandas pillow pylatex customtkinter pyinstaller
clear

echo "Creando el binario con PyInstaller..."
pyinstaller --hidden-import=PIL._tkinter_finder --onefile metric3.py
clear

echo "Montando el binario en el sistema..."
# Obtener el directorio actual
current_dir=$(pwd)

# Obtener el directorio del usuario
# user_dir=$(eval echo ~$USER)

# Crear el enlace simbólico
sudo ln -s "$current_dir/dist/metric3" "/usr/local/bin/metric3"
clear

echo "Instalación completa."
