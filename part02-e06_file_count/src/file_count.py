#!/usr/bin/env python3
"""
Parte 1.

Cree una función file_countque obtenga un nombre de archivo como parámetro y 
devuelva un triple de números. La función debe leer el archivo, contar el 
número de líneas, palabras y caracteres en el archivo y 
devolver un triple con estos recuentos en este orden. Obtienes división en
palabras dividiendo en espacios en blanco. No es necesario que elimines la
puntuación.

Parte 2.

Cree una función principal que en un bucle llame file_countusando cada nombre 
de archivo en la lista de parámetros de línea de comando sys.argv[1:]como 
parámetro, a su vez. Para llamar, la salida debe serpython3 src/file_count
file1 file2 ...

?      ?       ?       file1
?      ?       ?       file2
...
Los campos están separados por tabulaciones ( \t). Los campos están en orden:
recuento de líneas, recuento de palabras, recuento de caracteres, nombre de
archivo.
Para ejecutarlo pasar como parametro en la linea de comandos el archivo con argv[1:]
"""
import sys

def file_count(filename):
    lines = 0
    words = 0
    chars = 0
    with open(filename) as f:
        for l in f:
            lines += 1
            words += len(l.split())
            chars += len(l)
    
    return (lines, words, chars)

def main():
    for p in sys.argv[1:]:
        lines, words, chars = file_count(p)
        print(f"{lines}\t{words}\t{chars}\t{p}")    
if __name__ == "__main__":
    main()
