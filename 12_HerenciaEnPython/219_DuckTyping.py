###Esto es sobre el tema de polimorfismo
"""
    El polimorfismo es uno de los pilares básicos en la programación
    orientada a objetos, por lo que para entenderlo es importante
    tener las bases de la POO y la herencia bien asentadas.

    
    El término polimorfismo tiene origen en las palabras poly (muchos) y morfo (formas), y aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas. ¿Pero qué significa esto?

Pues bien, significa que objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos.

En lenguajes de programación como Python, que tiene tipado dinámico, el polimorfismo va muy relacionado con el duck typing.

Sin embargo, para entender bien este concepto, es conveniente explicarlo desde el punto de vista de un lenguaje de programación con tipado estático como Java. Vamos a por ello.







"""



class Animal:
    def hacer_sonido(self):
        print("Hago un pitido")


class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")


class Gato(Animal):
    def hacer_sonido(self):
        print("Puedo maullar")

# Funcion polimorfica
def hacer_sonido_animal(animal): #duck typing
    animal.hacer_sonido()


print("** Ejemplo Polimorfismo")
print("Clase Padre Animal: ")

animal1 = Animal()
hacer_sonido_animal(animal1)

# Definimos un objeto de la clase Perro
print("\nClase Hija perro: ")

perro1 = Perro()
hacer_sonido_animal(perro1)

# Definimos un objeto de la clase Gato
print('\nClase Hija Gato: ')
gato1 = Gato()
hacer_sonido_animal(gato1)
