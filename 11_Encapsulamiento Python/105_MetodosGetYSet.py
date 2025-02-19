# get = obtener/recuprar
# set = colocar/modificar

# decorador


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property  # Esto es un decorador, modifica el comportamiento de nuestro metodo y con esto metodo podemos seguir accediendo
    def nombre(self):
        print(
            "Llamando método get nombre"
        )  # comprobacion para saber si estamos llamando estos parametros
        return self._nombre

    @nombre.setter  # aqui se puso el nombre del atributo y con esto estamos diciendo que esta asociado con atributo nombre(no es necesario el _)
    def nombre(self, nombre):  # y tambien estamos indicando que es tipo set
        print("Llamando método set nombre")
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


persona1 = Persona("Juan", "Perez", 28)
persona1.nombre = "Juan Carlos"
print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)
