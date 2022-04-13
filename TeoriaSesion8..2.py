class Juguete:
    nombre =" "
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio


    def __str__(self): #SALIDA NORMAL
        return f'Mi nombre es {self.nombre} y mi precio {self.precio}'

    def __repr__(self): #SALIDA TECNICA
        return f'Potato({self.nombre},{self.precio})'


j1=Juguete("Potato",10.5)
j2=Juguete("Dino",3.4)
print(str(j1))
print(repr(j1))

print(j1) #llama a str()  por debajo
representacionTextual=str(j1)
print(representacionTextual)
print(j2)

import pprint
pprint.pprint(dir('')) #metodos que se pueden utilizar con una cadena

cadena="En un lugar de la Mancha"
numero="a"
print(cadena.capitalize())
print(cadena.title())
print(cadena.count())
print(cadena.count('a'))
print(cadena.lower())
print(cadena.lower().count('a'))

otracadena=cadena.lower()
print(otracadena.count('a'))

print(cadena.format())
print(numero.isdigit())
print(numero.isalnum())
print(numero.isalpha())

cadena="       en un lugar de la manchA"
print(cadena.lower().endswith("mancha"))
print(cadena.split('en'))
print(cadena)
print(cadena.strip())