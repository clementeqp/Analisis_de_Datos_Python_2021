#!/usr/bin/env python3
"""
El archivo src/listing.txtcontiene una lista de archivos con una línea por archivo.
Cada línea contiene siete campos: derechos de acceso, número de referencias,
nombre del propietario, nombre del grupo propietario, tamaño
del archivo, fecha, nombre del archivo. Estos campos están separados por uno o más 
espacios. Tenga en cuenta que también puede haber espacios dentro de estos siete 
campos.

Función de escritura file_listingque carga el archivo src/listing.txt. Debería 
devolver una lista de tuplas (tamaño, mes, día, hora, minuto, nombre de archivo). 
Utilizar expresiones regulares para hacer esto (ya sea match, search, findall, o finditermétodo).
"""
import re


def file_listing(filename="src/listing.txt"):
    lista=[]
    with open(filename,'r') as file:
        for linea in file:
            l=re.findall(r'\S*\s\d\s\S*\s\S*\s*(\d*)\s([A-Za-z]{3})\s*(\d*)\s(\d\d):(\d\d)\s(\S*)', linea)
            #r".{10}\s+\d+\s+.+\s+.+\s+(\d+)\s+(...)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)"
            l_trans=(int(l[0][0]), l[0][1], int(l[0][2]), int(l[0][3]), int(l[0][4]), l[0][5])
            lista.append(l_trans)
    
    return lista

"""
Propuesta
import re
 
 
def file_listing(filename="src/listing.txt"):
    with open(filename) as f:
        lines = f.readlines()
    result=[]
    for line in lines:
        pattern = r".{10}\s+\d+\s+.+\s+.+\s+(\d+)\s+(...)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)"
        if True:      # Two alternative ways of doing the same thing
            m = re.match(pattern, line)
        else:
            compiled_pattern = re.compile(pattern)
            m = compiled_pattern.match(line)
        if m:
            t = m.groups()
            result.append((int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]))
        else:
            print(line)
    return result
 
def main():
    tuples = file_listing()
    for t in tuples:
        print(t)
"""


def main():
    L=file_listing()
    for l in L:
        print(l)

if __name__ == "__main__":
    main()
