#!/usr/bin/env python3
"""
Crea una función word_frequenciesque obtiene un nombre de archivo como parámetro 
y devuelve un dictado con las frecuencias de palabras. En el diccionario, 
las claves son las palabras y los valores correspondientes son el número de veces
que esa palabra apareció en el archivo especificado por el parámetro de función. 
Lea todas las líneas del archivo y divida las líneas en palabras usando el 
split()método. Además, elimine la puntuación de los finales de las palabras 
mediante la strip(\"\"\"!"#$%&'()*,-./:;?@[]_\"\"\")

Pruebe esta función en la función principal utilizando el archivo alice.txt. 
En la salida, debe haber una palabra y su recuento por línea separados por una
pestaña:

The     64
Project 83
Gutenberg   26
EBook   3
of      303

"""
import string
"""
def word_frequencies(filename):
    contadas={}
    file=open(filename,'r')
    for line in file:
        for l in line.split():
            l=l.strip(string.punctuation)
            if l in contadas:
                contadas[l]=contadas[l]+1
            else:
                contadas[l]=1    
        
        
    return contadas

def main():
    file="src/alice.txt"
    result=word_frequencies(file)
    for k,v in result.items():
        print(k,\t,v)
"""
def word_frequencies(filename):
    result = {}
    with open(filename) as in_file:
        for w in in_file.read().split():
            ws = w.strip("""!"#$%&'()*,-./:;?@[]_""")
            if ws not in result:
                result[ws] = 0
            result[ws] += 1
    return result
 
def main():
    for word, count in word_frequencies("src/alice.txt").items():
        print(f"{word}\t{count}")
 



if __name__ == "__main__":
    main()
