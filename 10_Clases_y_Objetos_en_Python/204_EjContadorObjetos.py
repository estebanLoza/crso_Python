#*Continuación del archivo 203 sobre atributos clase


class Persona:
    #atributo de clase
    contador_personas = 0 
    def __init__(self, nombre, apellido):
        #Incrementamos el valor del atributo de clase 
        Persona.contador_personas += 1