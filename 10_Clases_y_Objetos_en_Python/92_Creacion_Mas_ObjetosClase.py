#LAS CLASES SE CREAN CON EL NOMBRE DEL ARCHIVO, COMO BUENA PRACTICA

class Persona: #CLASE
    def __init__(self, nom, apellido, edad):  
        self.nombre = nom   #*No importa si el parametro no sea igual al del self->(atributo)
        self.apellido =  apellido
        self.edad = edad
    pass



        

persona1 = Persona("Juan", "Apellido", 25) #PRIMER OBJETO

print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f'{persona1.edad}')


persona2 = Persona("Karla", "Gomez", 30) #SEGUNDO OBJETO
print(f"Objeto PERSONA 2 {persona2.nombre} {persona2.apellido} {persona2.edad}")


#AQUI SE crearon 2 objetos desde la plantilla Persona
#si queremos acceder a otra plantilla debemos crear otra clase
