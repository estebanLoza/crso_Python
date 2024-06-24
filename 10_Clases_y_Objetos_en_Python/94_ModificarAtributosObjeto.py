class Persona:
    def __init__(self, nom, apellido,edge):
        self.nombre = nom
        self.apellido = apellido
        self.edad = edge
        pass


persona1 = Persona("Juan", "Hernandez", 25)
print(f"Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}")

persona2 = Persona("Karla", "Chavez", 15)
print(f"Objeto Person 2: {persona2.nombre} {persona2.apellido} {persona2.edad}")


print('\n')


#MODIFIACAR LOS VALORES UNA VES QUE HAYAMOS CREADO EL OBJETO Y SUS VALORES

persona1.nombre = "Esteban"
persona1.edad = 30
persona1.apellido = "Loza"

print(f"La modificacion de la Clase es: {persona1.nombre} {persona1.apellido} {persona1.edad}")


persona2.nombre = "Leslie"
persona2.apellido = "Ramireza"
persona2.edad = 13

print(f"La modificacion de la CLASE 2 es: {persona2.nombre} {persona2.apellido} {persona2.edad}")



# ESTO NO ES LO RECOMENDABLE PARA HACERLO, OSEA ACCEDER DIRECTAMENTE, SINO USAR EL METODO DE ENCAPSULAMIENTO





