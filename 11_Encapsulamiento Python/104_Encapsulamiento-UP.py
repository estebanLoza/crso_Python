# el encapsulamiento (o atributo encapsulamiento) es el siguiente "_" que es un guion bajo, con esto indicamos que no podemos
# acceder directamente al valor de ese atributo, solamente la clase puede acceder. Pero si estamos afuera de nuestra clase no
# podemos hacerlo


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


persona1 = Persona("Juan", "Perez", 28)
# persona1.nombre = 'Juan Carlos'   #Esto es un dato de tipo publico y podemos acceder directamente (QUE NO ESTA BIEN)
persona1._nombre = "Juan Carlos"
persona1.mostrar_detalle()
