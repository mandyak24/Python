numero=511
texto="quijote"
otromas=1.2

#print("El numero es %d y el texto es %s y tiene %f" % (numero,texto,otromas))
#print("Valor flotante: %2f" % otromas)
print("El numero es {0} y el texto es {1} y tiene {2}"
    .format(numero,texto,otromas)
)

def suma(a,b):
    return a+b

txt=f'El numero es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}'
print(txt)


print(str(511)) #convertir un numero en una cadena String
