""" 
    *****METODOS Y ESTANCIA DE UNA CLASE ****

    METODOS = es el comportamiento que va a tener nuestros objetos

            ? ***NOTA***
            ? Un método es igual que una función. Pero se le llama método
            ? por que se asocia con una clase

            ??UML

"""


class Persona:
    def __init__(self, nombre, apellido, edad):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):  # * **self** se agrega a todos los metodos de instancia

        # mandamos a imprimir la siguiente información

        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")
        # esto nos podria ayudar a imprimir todo sin la necesidad de lo otro como la variable
        # persona1 (archivos 90 al 94)
        pass


persona1 = Persona("Juan", "Hernandez", 40)

persona1.mostrar_detalle()

persona2 = Persona("Karla", "Gomez", 30)

persona2.mostrar_detalle()
