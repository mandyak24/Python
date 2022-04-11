class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota


    def alumnoNota(self):
       print(f"Hola,{self.nombre} tu nota es un {self.nota}")
        
alumno0=Alumno("Amanda",7.6)

alumno0.alumnoNota()
