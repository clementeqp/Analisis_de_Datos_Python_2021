#!/usr/bin/env python3
"""
Cree una función llamada summaryque obtenga un nombre de archivo como parámetro. 
El archivo de entrada debe contener un número de punto flotante en cada línea del
archivo. Haga que su función lea estos números y luego devuelva un triple que 
contenga la suma, el promedio y la desviación estándar de estos números para el
archivo. Como recordatorio, la fórmula para la desviación estándar muestral
corregida es∑ni=1(xi−x¯¯¯)2n−1−−−−−−−−√, dónde x¯¯¯ es el promedio.

La mainfunción debe llamar al resumen de la función para cada nombre de archivo 
en la lista sys.argv[1:]de parámetros de la línea de comandos. 
(Omita sys.argv[0]ya que contiene el nombre del programa actual).

Ejemplo de uso desde la línea de comandos: python3 src/summary.py src/example.txt
src/example2.txt

Imprima números de coma flotante con una precisión de seis decimales. La salida 
debería verse así:

File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
File: src/example2.txt Sum: 5446.200000 Average: 1815.400000 Stddev: 3124.294045
"""

import sys
import math


def summary(filename):
    numbers=[]
    with open(filename,'r') as f:
        for n in f:
            try:
                numbers.append(float(n))
            except ValueError:
                print("Not a float")
# suma
    suma=sum(numbers)
                
# Media 
    media=suma/len(numbers)
    
    
# Desviacion
    dif2=0 
    for n in numbers:
        dif2=(n-media)**2+dif2
    desviacion=math.sqrt(dif2/(len(numbers)-1))
    
    return (suma, media, desviacion)

def main():
    
    for s in sys.argv[1:]:        
        suma, media, desviacion = summary(s)
        print(f"File: {s} Sum: {suma:.6f} Average: {media:.6f} Stddev: {desviacion:.6f}")
"""
Propuesta
 
from statistics import stdev
import sys
 
def summary(filename):
    L=[]
    with open(filename) as f:
        for line in f:
            try:
                L.append(float(line))
            except ValueError:
                continue
    s = sum(L)
    a = s/len(L)
    stddev = stdev(L)
    return s, a, stddev
 
def main():
    for filename in sys.argv[1:]:
        s, a, stddev = summary(filename)
        print(f"File: {filename} Sum: {s:.6f} Average: {a:.6f} Stddev: {stddev:.6f}")


C:/anaconda3/python.exe c:/Users/Propietario/AppData/Local/tmc/vscode/hy-data-analysis-with-python-summer-2021/part02-e05_summary/src/summary.py src/example.txt src/example2.txt src/example3.txt


"""

if __name__ == "__main__":
    main()
