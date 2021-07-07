#!/usr/bin/env python3
"""
Escribe una función sum_equationque tome una lista de números enteros positivos como parámetros y devuelva una cadena con una ecuación de la suma de los elementos.

Ejemplo: sum_equation([1,5,7])devuelve Observe, los espacios deben ser exactamente como se muestra arriba. Para una lista vacía, la función debe devolver la cadena "0 = 0"."1 + 5 + 7 = 13"


"""
def sum_equation(L):
    if not L:
        result="0 = 0"
    else:
        result= list(map(str,L))
        #print(result)
        result = " + ".join(result) + f" = {sum(L)}"
    
    return result

def main():
    print(sum_equation([1,5,7]))
    

if __name__ == "__main__":
    main()
