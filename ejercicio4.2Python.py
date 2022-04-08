#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]


numeroInicio=0
while numeroInicio <100:

    if numeroInicio%2!=0:
        print(numeroInicio)
    
    numeroInicio+=1

