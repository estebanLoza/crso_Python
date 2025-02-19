#CLASE 113 SOBRE COMO HACER UNA HERENCIA CON LA CLASE PADRE

class Persona: #clase padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona:{self.nombre} {self.edad}" 
#modificacion de la clase 113 sobre la importacion






#definir una clase hija
class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        #llamando el constructor de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'