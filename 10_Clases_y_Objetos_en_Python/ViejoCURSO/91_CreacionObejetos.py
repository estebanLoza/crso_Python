# LAS CLASES SE CREAN CON EL NOMBRE DEL ARCHIVO, COMO BUENA PRACTICA


class Persona:  # CLASE, las clases se inician en Mayusculas
    def __init__(self, nom, apellido, edad):
        self.nombre = (
            nom  # *No importa si el parametro no sea igual al del self->(atributo)
        )
        self.apellido = apellido
        self.edad = edad


persona1 = Persona("Juan", "Apellido", 25)  # PRIMER OBJETO

print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")


# *Manerra 2 para ver que no importa que el parametro no sea igual al self->(atributo) (que es el del lado derecho)


# class Persona: #clase
#     def __init__(self, nom, apellido, edad):
#         self.name = nom #*No importa si el parametro no sea igual al del self->(atributo)
#         self.lastName = apellido #*No importa si el parametro no sea igual
#         self.age = edad

# persona1 = Persona("Juan", "Apellido", 23) #Primer objeto

# print(f"{persona1.name}")
# print(f"{persona1.lastName}")
# print(f"{persona1.age}")


""""class Personass:
    def __init__(self, nombree, apellido, apellidoPaterno):
        self.naaaamme = nombree
        self.apelliido = apellido
        self.apelliidoPaterno = apellidoPaterno


person2 = Personass("Pedrito", "Hernandez", "Loza")


print(f"{person2.naaaamme}")
print(f"{person2.apelliido}")
print(f"{person2.apelliidoPaterno}")"""
