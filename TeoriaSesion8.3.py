#CONJUNTO DE FUNCIONES DE MANIPULACION DE FICHEROS 
f=open('C:\Users\Lenovo\OneDrive\Escritorio\OBC','r')
datos=f.read()
datos=f.readline() #consume , me devuelve la primera linea
f.close


#COMO LEEER UN FICHERO:
datos="a"
while datos != "":
    datos.f.readline()
    print(datos)

f.close()

#OTRA FORMA:

f=open('','r')
datos=f.readlines()
f.close

print(datos)





#r : lectura
#a :append (adjuntar)
#w : escritura
#x : create

#t : texto
#b : binary

# +