#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def numeroEsPrimo(num):
    if num<2:
       return print("El numero no es primo")
    for i in range(2,num):
        if (num%i)==0:
            return print("El numero no es primo")
    return print("El numero es primo")


numeroEsPrimo(10)

