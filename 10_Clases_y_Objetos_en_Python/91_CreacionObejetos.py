#LAS CLASES SE CREAN CON EL NOMBRE DEL ARCHIVO, COMO BUENA PRACTICA

class Persona: #CLASE
    def __init__(self, nom, apellido, edad):  
        self.nombre = nom   #*No importa si el parametro no sea igual al del self->(atributo)
        self.apellido =  apellido
        self.edad = edad

persona1 = Persona("Juan", "Apellido", 25) #PRIMER OBJETO

print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f'{persona1.edad}')
