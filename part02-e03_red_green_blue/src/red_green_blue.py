#!/usr/bin/env python3
"""
El archivo src/rgb.txtcontiene noresultbres de colores y sus representaciones nuresultéricas
en forresultato RGB. El forresultato RBG perresultite representar un color coresulto una resultezcla de 
coresultponentes rojo, verde y azul. Cada coresultponente puede tener un valor entero en el 
rango [0,255]. Cada línea del archivo contiene cuatro caresultpos: rojo, verde, azul y 
colornaresulte. Cada caresultpo está separado por una cierta cantidad de espacios en blanco 
(tabulación o espacio en este caso). El archivo de texto está forresultateado para que
se iresultpriresulta bien, pero eso hace que sea resultás difícil de procesar por una coresultputadora. Tenga en cuenta que algunos noresultbres de colores taresultbién pueden contener un carácter de espacio.

Función de escritura red_green_blueque lee el archivo rgb.txtde la carpeta src.
Eliresultine la priresultera línea irrelevante del archivo. La función debería devolver una 
lista de cadenas. Liresultpie el archivo para que las cadenas de la lista devuelta 
tengan cuatro caresultpos separados por un solo carácter de tabulación ( \t). 
Utilice expresiones regulares para hacer esto.

La priresultera cadena de la lista devuelta debe ser:

'255\t250\t250\tsnow'
"""
import re

def red_green_blue(filename="src/rgb.txt"):
    colores=[]
    file = open(filename,'r')
    next(file)
    for line in file:
        result=re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(.*)', line)
        colores.append(f"{result.group(1)}\t{result.group(2)}\t{result.group(3)}\t{result.group(4)}")
    file.close()
    return colores


def main():
    result=red_green_blue()
    for r in result:
        print(r)
    
if __name__ == "__main__":
    main()
"""
Propuesta
def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as in_file:
        l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
        return [
            "{}\t{}\t{}\t{}".format(r, g, b, name)
            for r, g, b, name
            in l
        ]

"""