"""
    La programacion orientada a objetos tiene 6  pilares o principios basicos:

        * Herencia
        * Cohesion
        * Abstraccion
        * Polimorfismo
        * Acoplamiento
        * Encapsulamiento
    
    Existen 2 atributos a nuestra clase.
        * Atributos 'instancia' ---> Pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada instancia
                                     en nuestro caso de cada perro (mira el codigo 1) 
                                    (sera el nombre y la raza) mira el codigo 1


        * Atributos 'clase' ------> Se trata atributos que pertenecen a la clase, por lo tanto seran comunes para todos los objetos 
                                    (sera comun para para todos los perros, que son especie, que es algo comun en todos los perros)

"""





class Perro:

    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        #*Atributos de instancia
        self.nombre = nombre
        self.raza = raza 



#Creando un objeto (el perro)

mi_perro = Perro("Toby", "Bulldog")
print(type(mi_perro))


print(mi_perro.nombre)
print(mi_perro.raza)


