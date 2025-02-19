#**Tema sobre READ ONLY en python


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property #sirve para decire que se un atributo o propiedad
    def nombre(self):
        print("Llamado método get hombre")
        return self._nombre 
                                #readOnly  esto esto es solo diciendo que sirve solo para lectura y no podemos asociar o tener los valores
    
    # @nombre.setter
    # def nombre(self, nombre):
    #     print("Llamado método set nombre")
    #     self._nombre = nombre
    
    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")
    

    

persona1 = Persona("Juan", "Perez", 28)
persona1.nombre = "Juan Carlos"
print(persona1.nombre)
