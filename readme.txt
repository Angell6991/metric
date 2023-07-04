 #####################################################################
#######################################################################
###       							    ###
###  MMM       MMM  EEEEEE  TTTTTTTT   RRRRRRR   IIIIII      CCCCC  ###
###  MM MM   MM MM  EE         TT      RR     R    II      CCC      ###
###  MM  MM MM  MM  EE         TT      RR     R    II     CC        ###
###  MM    M    MM  EEEEEE     TT      RRRRRRR     II    CC         ###
###  MM         MM  EE         TT      RR  RR      II     CC        ###
###  MM         MM  EE         TT      RR   RR     II      CCC      ###
###  MM         MM  EEEEEE     TT      RR    RR  IIIIII      CCCCC  ###
### 						           	    ###
#######################################################################
 #####################################################################


#######################################################################
##------------------------INSTRUCTIONS-------------------------------##
#######################################################################


Para la inplementacion del programa se requieren las tres partes 
metric1.py, metric2.py y metric3.py  

Y para su ejecuacion mediante el interprete de python se debe de 
ejecutar metric3.py

librerias python:
sympy
pylatex
customtkinter
Pillow

Adicionalmente se requiere tener instalado LateX y zathura los cuales 
se pueden instalar en arch linux con:

sudo pacman -S zathura
sudo pacman -S texlive-most


#######################################################################
##--------------------------COMPILATOR-------------------------------##
#######################################################################

Install compilador python:
pip install pyinstaller 

compilar python:
pyinstaller nombre_archivo.py
pyinstaller --onefile nombre_archivo.py

para montar el ejecutable en el sistema hay que moverlo á alguna rutas
mostradas con el comando:

echo $PATH

#------------------------------IGNORE---------------------------------#

compilar latex : 
pdflatex nombre_del_archivo.tex

buscar ruta de un programa:
which nombre_programa



