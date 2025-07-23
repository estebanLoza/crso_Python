"""
La herencia es un proceso mediante el cual se puede crear una clase 
hija que hereda de una clase padre, compartiendo sus métodos y atributos. 

Además de ello, una clase hija puede sobreescribir los métodos o atributos, 
o incluso definir unos nuevos.

Se puede crear una clase hija con tan solo pasar como parámetro la clase de la que queremos heredar. 
En el siguiente ejemplo vemos como se puede usar la herencia en Python, 
con la clase Perro que hereda de Animal. Así de fácil.


# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass

"""

# Esto es una prueba


class Animal:

    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print("Duermo muchas horas")


# clase hija, aquí se hace la herencia de la clase Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")


# Programa principal
print("** El ejemplo de Herencia en python ** ")
print("Clase Padre, soy un Animal")
animal1 = Animal()
animal1.comer()
animal1.dormir()


print("\nClase hija, soy un Perro")
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
