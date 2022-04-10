#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

from cmath import pi
import math

def areaTriangulo(base,altura):
   
   return (base*altura)/2

print(areaTriangulo(10,12))


def areaCirculo(radio):
    
    area = pi*math.pow(radio,2)
    print("El area del circulo de radio {0} es {1}".format(radio,area)) 
    
    
areaCirculo(12)
