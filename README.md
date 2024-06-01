<p align="center">
  <img src="logo_doc/logo.png"  width="250">
</p>


<h2 align="center"> Metric3 </h2>


## Descripción
Metríc3 es un proyecto desarrollado en Python desde Fedora 40 y configurado esencialmente para el 
window manager BSPWM, con compatibilidad en cualquier sistema operativo de Linux. Se encarga de 
realizar los cálculos de los símbolos de Christoffel, el tensor de Riemann, el tensor de Ricci y 
el escalar de curvatura.

Las características distintivas de este proyecto son que, para realizar los cálculos mencionados 
anteriormente, hace uso de una interfaz de usuario que permite introducir de manera explícita el 
tensor métrico. Para el despliegue de resultados, utiliza LaTeX para construir un documento PDF 
que contiene los resultados de los cálculos en lenguaje matemático y ordenados de forma matricial.


## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)


## Instalación
La guía de instalación de Metric3 la desarrollaremos para Fedora, simplemente por ser el entorno en el 
que se desarrolló. Por lo tanto, los comandos de instalación estarán orientados al uso del gestor de 
paquetes RPM. Sin embargo, si eres usuario de distribuciones basadas en Arch o Debian, bastará con 
hacer uso de los gestores de dichas distribuciones.


### Intalación manual

#### Prerrequisitos
Como requisito previo para instalar Metric3 en el sistema, se necesita tener instalados el 
visor de PDF zathura, el lenguaje de programación Python, el gestor de paquetes de Python 
pip y el sistema de composición de texto LaTeX.

Para instalar Python, pip y zathura, simplemente utiliza el siguiente comando en la terminal:
```sh
sudo dnf install python python-pip zathura
```

Para la instalación de LaTeX, se sugiere seguir la 
[Documentación de LaTex en Fedora](https://docs.fedoraproject.org/en-US/neurofedora/latex/)
,y se recomienda instalar Texlive-full. Sin embargo, al ser una instalación más completa, 
hay que tener en cuenta que esta instalación llevará un tiempo considerable.


#### Librerías de python 

Instala tkinter con: 
```sh
sudo dnf install python-tkinter 
```

Instala sympy, pandas, pillow, pylatex, customtkinter y pyinstaller con pip:
```sh
pip install sympy pandas pillow pylatex customtkinter pyinstaller
```

#### Clonar el repositorio
Una vez instalados los programas y librerías anteriores, se procede a clonar 
el repositorio en la ruta:
```sh
git clone https://github.com/Angell6991/metric.git ~/.config/metric
```

Ya que se ha clonado el repositorio, se puede ejecutar el programa sin necesidad 
de montarlo en el sistema, a través del intérprete de Python. Solo hay que dirigirse 
al directorio en el cual se clonó el repositorio:
```sh
cd ~/.config/metric
```
Y para iniciar el programa con el intérprete de Python, se ejecuta en la terminal:
```sh
python metric3.py 
```
De esta forma, el programa ya sería usable. Sin embargo, si se desea ejecutarlo 
desde cualquier parte del sistema, te invito a seguir con la guía de instalación.


#### Montando Metric3 con pyinstaller
Una vez clonado el repositorio, nos dirigimos al directorio de guardado:
```sh
cd ~/.config/metric
```
Creamos el binario haciendo uso de PyInstaller:
```sh
pyinstaller --hidden-import=PIL._tkinter_finder --onefile metric3.py
```
Ten presente que este proceso puede llevar un tiempo.




## Uso
```sh
```
