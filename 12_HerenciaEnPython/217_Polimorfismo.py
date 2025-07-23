"""
    #Polimorfismo
    
    El término polimorfismo tiene origen en las palabras poly (muchos) y morfo (muchas), y aplicando a la programación
    hace referencia a que los objetos pueden tomar diferentes formas. ¿Pero que signfica esto?.

    Pues bien, significa que objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando 
    un comportamiento distinto(tomando diferentes formas) según cómo sean accedidos.


    

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


print("** Ejemplo Polimorfismo")
print("Clase Padre Animal: ")

animal1 = Animal()
animal1.hacer_sonido()

# Definimos un objeto de la clase Perro
print("\nClase Hija perro: ")

perro1 = Perro()
perro1.hacer_sonido()  # Polimorfismo

# Definimos un objeto de la clase Gato
print('\nClase Hija Gato: ')
gato1 = Gato()
gato1.hacer_sonido()
