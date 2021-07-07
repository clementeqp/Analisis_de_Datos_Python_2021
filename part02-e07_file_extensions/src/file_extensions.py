#!/usr/bin/env python3

"""
Función de escritura file_extensionsque obtiene como 
parámetro un nombre de archivo. Debería leer las líneas 
de este archivo. Cada línea contiene un nombre de archivo. 
Busque la extensión para cada nombre de archivo. 
La función debería devolver un par, donde el primer 
elemento es una lista que contiene todos los nombres 
de archivo sin extensión 
(con el punto anterior ( .) eliminado). 
El segundo elemento del par es un diccionario con extensiones
como claves y los valores correspondientes son listas con nombres 
de archivo que tienen esa extensión.

Suena un poco complicado, pero es de esperar que el siguiente ejemplo 
aclare esto. Si el archivo contiene las siguientes líneas

file1.txt
mydocument.pdf
file2.txt
archive.tar.gz
test
entonces el valor de retorno debe ser el par: 
(["test"], { "txt" : ["file1.txt", "file2.txt"], 
"pdf" : ["mydocument.pdf"], "gz" : ["archive.tar.gz"] } )

Parte 2.

Escriba un mainmétodo que llame a la file_extensionsfunción con 
"src / filenames.txt" como argumento. Luego imprima los resultados 
de modo que para cada extensión haya una línea que consta de la extensión
y el número de archivos con esa extensión. La primera línea de la 
salida debe dar la cantidad de archivos sin extensiones.

Con el ejemplo de la parte 1, la salida debe ser

1 files with no extension
gz 1
pdf 1
txt 2

"""


def file_extensions(filename):
    
    dic={}
    lista=[]
    with open(filename)as file:
        for line in file:
            line=line.strip()
            if '.' in line:
                l=line.split('.')
                ext=l[-1].strip()
                value=line.strip()
                if ext not in dic:
                    dic[ext]=[]
                    dic[ext].append(line)
                else:
                    dic[ext].append(value)
                    
            else:
                lista.append(line.strip())
    print(lista, dic)
    
    return (lista, dic)
"""
import re

def file_extensions(filename):

    with open(filename) as f:
        ext = {}
        non_ext = []
        for name in f:
            match = re.match(r'(.+)\.(.+)\n',name)
            if match:
                if match.group(2) in ext:
                    ext[match.group(2)].append(match.group(0)[:-1])
                else:
                    ext[match.group(2)] = [match.group(0)[:-1]]
            else:
                non_ext.append(name[:-1])
    return (non_ext, ext)
"""
def main():
    filename = "src/filenames.txt"
    lista, dic = file_extensions(filename)
    print(f"{len(lista)} files with no extension")
    for k in sorted(dic.keys()):
        print(f"{k} {len(dic[k])}")

if __name__ == "__main__":
    main()
