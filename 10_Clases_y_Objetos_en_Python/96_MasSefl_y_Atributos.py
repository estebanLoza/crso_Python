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
# MANERA DE AGREGAR UN ATRIBUTO NO ES POSIBLE DE LA SIGUIENTE MANERA YA QUE NO ESTA EN LA CLASE (SOLO SE PODRA EN PERSONA1 NO EN 2)
persona1.telefono = "44323423"
print(persona1.telefono)

# OTRA FORMA DE IMPRIMIR
# Persona.mostrar_detalle(persona1) #Esto no es comun

persona2 = Persona("Karla", "Gomez", 30)

persona2.mostrar_detalle()

# print(pesona2.telefono) no se podra por que solo se creo en la linea 22
