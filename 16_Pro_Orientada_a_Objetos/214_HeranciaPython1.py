"""
    **** Herencia Python Parte 1

    La herencia es como cuando una hija o hijo hereda cosas de
    sus padres.
    En programación, una clase puede heredar cosas (como funciones
    y variables) de otra clase.

    ¿Para qué sirve?

    Sirve para reutilizar código y organizarlo mejor


***********EJEMPLO DE CÓDIGO********


    #clase padre
    class Animal:
        def hablar(self):
            print("Este animal hace un sonido")

    #clase Hija

    class Perro(Animal):
        def hablar(self):
            print("El perro dice: ¡Guau!")

    #Otra clase hija
    class Gato(Animal):
        def hablar(self):
            print("El gato dice: ¡Miau!")

    #Usando las clases
    a = Animal()
    p = Perro()
    g = Gato()

    a.hablar()  #Este animal hace un sonido
    p.hablar()  #El perro dice: ¡Guau!
    g.hablar()  #El gato dice: ¡Miau!


*********FIN DEL CÓDIGO*************

    Qué pasó aquí?

    1 - Pero y Gato heredan de Animal
    2 - Usan el método hablar, pero lo modifican a su manera.
    3 - No necesitas reescribir todo, solo lo que cambia.



"""


class Animal:
    def comer(self):
        print("Como muchas veces el día")

    def dormir(self):
        print("Duermo muchas horas")


class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")
