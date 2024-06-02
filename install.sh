#!/bin/bash

echo "Instalando dependencias..."
sudo dnf install -y python python-pip zathura python-tkinter
clear

echo "Instalando librerías de Python..."
pip install sympy pandas pillow pylatex customtkinter pyinstaller
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
