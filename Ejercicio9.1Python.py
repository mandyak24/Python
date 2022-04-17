
#9.1..Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

paises=[]

print("Ingresa 3 paises")
for x in range(3):
    if x not in paises:
        ingresado = input("Ingrese:")  # Capturamos lo ingresado por teclado
        paises.append(ingresado)  # Agregamos al arreglo lo ingresado
        
paises.sort() #Ordenamos el arreglo alfabeticamente
convert_list_to_set = set(paises)
print("Ordenados alfabeticamente:")
print(convert_list_to_set)  # Mostramos



