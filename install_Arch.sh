#!/bin/bash

echo "Instalando dependencias..."
sudo pacman -S python python-pip python-sympy python-pandas python-pillow zathura zathura-pdf-mupdf zathura-ps zathura-djvu zathura-cb tk
clear

echo "Instalando librerías de Python..."
pip install pylatex customtkinter pyinstaller
clear

echo "Creando el binario con PyInstaller..."
pyinstaller --hidden-import=PIL._tkinter_finder --onefile ~/.config/metric/metric3.py
clear

# Moviendo Carpetas de construccion del binario
mv build ~/.config/metric/
mv dist ~/.config/metric/
mv metric3.spec ~/.config/metric/

echo "Montando el binario en el sistema..."
sudo ln -s ~/.config/metric/dist/metric3 /usr/local/bin/metric3
clear

echo "Instalación completa."
