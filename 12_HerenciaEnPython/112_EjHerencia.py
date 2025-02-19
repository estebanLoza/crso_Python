class Persona: #clase padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#definir una clase hija
class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        #llamando el constructor de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo


empleado1 = Empleado("Juan", 23, 500)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)