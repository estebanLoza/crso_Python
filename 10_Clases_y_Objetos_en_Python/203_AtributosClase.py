""""
**** Atributos de clase
Un atributo de clase es como una variable global dentro de la clase, ya que pertenece a la clase misma y no a los objetos individuales.
 Es compartido por todos los objetos de esa clase.

A diferencia de los atributos de instancia (que se crean dentro del __init__ con self), 
los atributos de clase se definen fuera de cualquier método, directamente dentro de la clase.


class Perro:

    especie = 'canino' #Atributo de clase #---> esto es el atributo de clase y esto es como una variable global dentro de la clase 

    def __init__(self, nombre):
        self.nombre  = nombre #Atributo de instancia 



"""""

class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


#programa principal 

if __name__ == "__main__":
 
    print(f"Atributo de clase ****")
    print(f'Atributo de clase: {Persona.atributo_clase}')

    # Modificamos el atributo de clase 
    Persona.atributo_clase = 10
    print(f'Atributo de clase : {Persona.atributo_clase}')



    # Creamos un objeto persona1
    persona1 = Persona(15)

    print(f"Atributo de clase persona1: {persona1.atributo_clase}")
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')
    
