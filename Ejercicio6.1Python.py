#Ejercicio 1

class Vehiculo():
    color=""
    ruedas=0
    puertas=0

    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculo):

    velocidad=0
    cilindrada=0

    def ___init__(self,velocidad,cilindrada):
      self.velocidad=velocidad
      self.cilindrada=cilindrada

#Coche objeto

coche=Coche("Azul",4,5)
