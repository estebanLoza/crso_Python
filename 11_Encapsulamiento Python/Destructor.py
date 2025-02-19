#Esto es de la clase 110


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad


    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")


    def __del__(self): #no es comun , pero estamos indicando hasta donde quermos que nosotros eleminamos
        print(f"Pesona: {self._nombre} {self._apellido} {self._edad}")






if __name__ == "__main__":
    persona1 = Persona("Juan", "Perez", 28)
    persona1.nombre = "Juan Carlos"
    print(persona1.nombre)
    persona1.apellido = "Lara"
    persona1.edad = 38
    persona1.mostrar_detalle()

print(__name__)