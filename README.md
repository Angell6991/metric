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
    - [Instalación automatizada](#instalación-automatizada)
    - [Instalación manual](#instalación-manual)
- [Desinstalación](#desinstalación)
- [Uso](#uso)


## Instalación
La guía de instalación de Metric3 la desarrollaremos para Fedora, simplemente por ser el entorno en el 
que se desarrolló. Por lo tanto, los comandos de instalación estarán orientados al uso del gestor de 
paquetes RPM. Sin embargo, si eres usuario de distribuciones basadas en Arch o Debian, bastará con 
hacer uso de los gestores de dichas distribuciones.


### Instalación automatizada
Dentro de la documentación se ha desarrollado un script el cual procede a instalar y configurar 
de manera automática el programa Metric3. Sin embargo, este instalador solo es 
para Fedora; en caso de usar distribuciones basadas en Arch o Debian, tendrá que seguir con la 
instalación manual.

#### Pasos instalación con el script 

Instalación de LaTeX, se sugiere seguir la 
[Documentación de LaTex en Fedora](https://docs.fedoraproject.org/en-US/neurofedora/latex/)
,y se recomienda instalar Texlive-full. Sin embargo, al ser una instalación más completa, 
hay que tener en cuenta que esta instalación llevará un tiempo considerable.

Clonar el repositorio:
```sh
git clone https://github.com/Angell6991/metric.git ~/.config/metric
```
Dar permisos de ejecución al script:
```sh
chmod u+x ~/.config/metric/install.sh
```
Ejecutar el script:
```sh
~/.config/metric/install.sh 
```
Si todo ha salido bien, ya podemos ejecutar el programa desde cualquier 
parte del equipo a través de:
```sh
metric3
```

### Instalación manual

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


#### Montando Metric3 con PyInstaller
Una vez clonado el repositorio, nos dirigimos al directorio de guardado:
```sh
cd ~/.config/metric
```
Creamos el binario haciendo uso de PyInstaller:
```sh
pyinstaller --hidden-import=PIL._tkinter_finder --onefile metric3.py
```
Ten presente que este proceso puede llevar un tiempo.

Una vez terminada la creación del binario, este se encontrará en el 
directorio "dist" recién creado dentro del directorio "metric". 
Para montar el binario en el sistema, lo realizaremos mediante un enlace simbólico: 
```sh
sudo ln -s ~/.config/metric/dist/metric3 /usr/local/bin/metric3
```
<!-- sudo ln -s /home/my_user/.config/metric/dist/metric3 /usr/local/bin/metric3 -->
<!-- Solo recuerda cambiar "my_user" por el nombre de usuario del equipo. -->

De esta manera, ya podemos ejecutar el programa desde cualquier parte del equipo 
a través de:
```sh
metric3
```

## Desinstalación
Si por alguna razón desea desinstalar el programa Metric3, es tan sencillo como 
seguir estos dos pasos:

Eliminar el directorio donde se clonó el repositorio:
```sh
rm -rf ~/.config/metric
```

Eliminar el enlace simbólico:
```sh
sudo rm /usr/local/bin/metric3
```

## Uso


<p align="left">
  <img src="logo_doc/var.png"  width="700">
</p>

texto de prueva

<p align="right">
  <img src="logo_doc/no_var.png"  width="700">
</p>

<p align="left">
  <img src="logo_doc/met.png"  width="700">
</p>

$$
\begin{equation}
ds^{2} = r^{2} d \psi^{2} + r^{2} \sin^{2} \psi \; d \theta^{2}  + r^{2} \sin^{2} \psi \sin^{2} \theta \; d \phi^{2}
\end{equation}
$$

```sh
```



