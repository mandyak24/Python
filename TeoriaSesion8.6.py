import pickle
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getNombre(self):
        return self.nombre

#GUARDAR ESTO DE FORMA QUE SE PUEDA RECUPERAR DESPUES
f=open('datos.bin','rb')
potato=pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), "precio: ", potato.precio)

class Estado:
    players=Players()
    status=Status()
    life_remaining=12
    armor=False
f=open('gamestatus.dat','rb')
e=pickle.load(f)
f.close()
