"""
 Modificar el comportamiento de la clase padre 
"""


class Animal:
    def comer(self):
        print("Como muchas veces al día")

    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")


# haciendo una sobrescritura


    def dormir(self):
        print('Duermo 15 horas al día')


# Programa principal
print("*** Ejemplo de Herencia en Python *** ")
print("Clase padre, soy un animal")
animal1 = Animal()
animal1.dormir()
animal1.comer()


# Clase hija y sobre escritura
print("\nClase hija, soy un perro")
perro1 = Perro()
perro1.comer()
perro1.dormir()  # Se llama el metodo sobre escritura de la clase hija
perro1.hacer_sonido()
