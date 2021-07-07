"""
Cree su propio módulo como archivo triangle.pyen la srccarpeta. El módulo debe contener dos funciones:

hypothenuse que devuelve la longitud de la hipotenusa cuando se dan las longitudes de otros dos lados de un triángulo rectángulo
area que devuelve el área del triángulo rectángulo, cuando dos lados, perpendiculares entre sí, se dan como parámetros.
Asegúrese de que tanto las funciones como el módulo tengan cadenas de documentación descriptivas. Agregue también los atributos __version__y __author__al módulo. Llame a ambas funciones desde la función principal (que está en el archivo usemodule.py).

"""



"Modulo Para calcular hipotenusa y area"

__version__= "1.0"
__author__= "Clemente"


import math


# Enter you module contents here
def hypothenuse(c1,c2):
    """Calcula hipotenusa conocidos los catetos"""
    return math.sqrt(c1**2+c2**2)    

def area(c1, c2):
    """Calcula el area de un triangulo rectangulo"""
    return c1*c2/2