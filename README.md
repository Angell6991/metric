<p align="center">
  <img src="logo_doc/logo.png"  width="250">
</p>


<h2 align="center"> Metric3 </h2>


## Descripción
Metríc3 es un proyecto desarrollado en Python con compatibilidad en cualquier sistema operativo de Linux. 
Se encarga de realizar los cálculos de los símbolos de Christoffel, el tensor de Riemann, el tensor 
de Ricci y el escalar de curvatura.

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
La guía de instalación de Metric3 la desarrollaremos para Arch. Por lo tanto, los comandos de 
instalación estarán orientados al uso del gestor de paquetes pacman. Sin embargo, si eres 
usuario de distribuciones basadas en Fedora o Debian, bastará con hacer uso de los gestores de 
dichas distribuciones.


### Instalación automatizada
Dentro de la documentación se ha desarrollado por el mometo dos scripts el cual procede a 
instalar y configurar de manera automática el programa Metric3, para Arch y Fedora  en caso 
de usar distribuciones basadas en Debian, tendrá que seguir con la instalación manual.

#### Pasos instalación con el script 

##### Prerrequisitos

Antes de instalar Metric3 se requiere tener LaTeX:

Para instalar Latex en Arch se recomienta hacer uso de pacman para buscar
y ver la disponibilidad de los paquetes de texlive

```sh
pacman -Ss texlive
```
De esta forma la instalacion la podras realizar de forma personalizada segun 
tus nesecidades, aun que se recomienda realizar una instalación tipo full
para evitar problemas de como falta de fonts o falta de compiladores de latex

Para dedora se sugiere seguir la 
[Documentación de LaTex en Fedora](https://docs.fedoraproject.org/en-US/neurofedora/latex/)
,y se recomienda instalar Texlive-full. Sin embargo, al ser una instalación más completa, 
hay que tener en cuenta que esta instalación llevará un tiempo considerable.


Una vez instalado Latex sin importar el tipo de distribucion de linux, clona el repositorio:
```sh
git clone https://github.com/Angell6991/metric.git ~/.config/metric
```

###### Arch
Dar permisos de ejecución al script:
```sh
chmod u+x ~/.config/metric/install_Arch.sh
```
Ejecutar el script:
```sh
~/.config/metric/install_Arch.sh 
```
Si todo ha salido bien, ya podemos ejecutar el programa desde cualquier 
parte del equipo a través de:
```sh
metric3
```
###### Fedora
Dar permisos de ejecución al script:
```sh
chmod u+x ~/.config/metric/install_Fedora.sh
```
Ejecutar el script:
```sh
~/.config/metric/install_Fedora.sh 
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
Para la guia de uso de Metric3 consideremos la metrica de una 3-esfera como ejemplo:

$$
ds^{2} \hspace{0.5em}=\hspace{0.5em} r^{2} \hspace{0.5em} d \psi^{2}  \hspace{0.5em}+\hspace{0.5em} r^{2} \sin^{2} \psi \hspace{0.5em} d \theta^{2}\hspace{0.5em}+\hspace{0.5em} r^{2} \sin^{2} \psi \sin^{2} \theta \hspace{0.5em} d \phi^{2}
$$

Cullos grados de livertad estan dados por las coordenadas: 

$$
x^{i} =
\begin{pmatrix}
\psi \\ 
\theta \\
\phi \\
\end{pmatrix}
$$

Una vez identificado esto de la metrica podemos empezar a usar Metric3 iniciandolo con: 
```sh
metric3
```
lo primero que mostrara el programa al iniciar es una ventana la cual pedira ingresar las variables, 
estas variables son las coordenadas que representan los grados de livertad de la metrica:

<p align="center">
  <img src="logo_doc/var.png"  width="800">
</p>

La forma de introducir la variables se muestra en la imagen anterior, es importante tener en cuenta 
que al ingresar los datos en el programa  solo idetifica la sintacxis de sympy de python.

una vez introducidas las variables damos a el boton "Next", con lo cual se despliega la siguente 
ventana:

<p align="center">
  <img src="logo_doc/no_var.png"  width="800">
</p>

En esta ventana se pide introducir las no variables, que en otras palabras son todos los parametros
que sn constantes de la metrica, como nuestra metrica es la de ua 3-esfera el radio "r" es constate
por lo que es en esta parte donde lo intrducimos. Es inportante tener en cuenta si la metrica posee
mas parametros constantes es en esta ventana donde se deben ingresar todos estas deominadas no variables
en dado caso que estes trabaad c ua metrica que pssea mas de un parametro constante estos se debe itrducir  
en forma de cloumna de la misma forma como se hace con las coordeadas e la ventana anterior.



$$
g_{ij} =
\begin{pmatrix}
r^{2} & 0 & 0 \\ 
0 & r^{2} \sin^{2} \psi & 0 \\
0 & 0 & r^{2} \sin^{2} \psi \sin^{2} \theta \\
\end{pmatrix} = \begin{pmatrix}
g_{11} & g_{12} & g_{13} \\ 
g_{21} & g_{22} & g_{23} \\
g_{31} & g_{32} & g_{33} \\
\end{pmatrix}
$$




<p align="center">
  <img src="logo_doc/met.png"  width="800">
</p>



```sh
```



