#!/usr/bin/env python3
"""
Escriba una función positive_listque obtenga una lista de números como parámetro y devuelva una lista con los números negativos y el cero filtrado usando la filterfunción.

La llamada a la función positive_list([2,-2,0,1,-7])debería devolver la lista [2,1]. Pruebe su función en la mainfunción.

 
def positive_list(L):
    return list(filter(lambda x: x > 0, L))
 
"""

def positive_list(L):
    return list(filter(get_positive,L))
    
def get_positive(l):
    return l>0

def main():
    L=([2,-2,0,1,-7])
    print(positive_list(L))
                  

if __name__ == "__main__":
    main()
