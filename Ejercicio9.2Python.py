#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada 
# por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce
import functools


miLista=[1,2,3,4,5,6,7,8,9,10]
def check_impares(number):
    if number %2 !=0:
        return True
    return False

check_impares_resultado=filter(check_impares,miLista)

numeros_impares=list(check_impares_resultado)

print(numeros_impares)

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, numeros_impares))
 