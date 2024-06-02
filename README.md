# Metric3


## INSTRUCTIONS
Para la inplementacion del programa se requieren las dos partes 
metric.py y metric3.py  

Y para su ejecuacion mediante el interprete de python se debe de 
ejecutar metric3.py

librerias python:

- sympy
- pandas
- pylatex

Adicionalmente se requiere tener instalado nvim, LateX y zathura los cuales 
se pueden instalar en arch linux con:

```sh
sudo pacman -S zathura
```

```sh
sudo pacman -S texlive-most
```

```sh
sudo pacman -S texlive-core
```

```sh
sudo pacman -S nvim 
```

## COMPILATOR

Install compilador python:
```sh
pip install pyinstaller 
```

compilar python:
```sh
pyinstaller nombre_archivo.py
```

```sh
pyinstaller --onefile nombre_archivo.py
```

para montar el ejecutable en el sistema hay que moverlo á alguna rutas
mostradas con el comando:
```sh
echo $PATH
```

## IGNORE

compilar latex : 
```sh
pdflatex nombre_del_archivo.tex
```

buscar ruta de un programa:
```sh
which nombre_programa
```



