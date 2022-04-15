#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.


class Vehiculo:

    ruedas=0
    color=""



    def __init__(self,ruedas,color):
        self.ruedas=ruedas
        self.color=color


vehiculo0=Vehiculo(5,"azul")
print(vehiculo0)