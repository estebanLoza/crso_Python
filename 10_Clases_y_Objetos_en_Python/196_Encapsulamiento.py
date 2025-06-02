"""
*** Encapsulamiento


    El encapsulamiento nos permite ocultar la información que almacena un objeto, también conocido como el estado del objeto.

    para aplicar el concepto de encapsulamiento se deben aplciar dos caracteristicas:

        1)Atributos protegidos o privados
            self._nombre #Atributo protegido
            self.__apellido #Atributo privadoo

        2) Crear los métodos conocidos como get (leer) y set (modificar)

"""

#! Recuerda que cuando usamos class el nombre de la clase incia con Mayusucla y el nombre del archivo py, debe de tener el mismo
# nombre para que tenga una buena practica


class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca  # Atribuot publico
        self._modelo = modelo  # Atributo protegido
        self.__color = color  # Atribtuo privado

    def conducir(self):
        # Como aún estamos dentro de la clase no hay necesidad de trabajar con get y set
        # se utiliza solo cuando salimos de la clase, en este caso es coche o tambien dentro del programa principal (abajo)
        print(
            f"""Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}"""
        )


# Programa principal

if __name__ == "__main__":
    # Creación de un primer coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()  # aunque no son publicos python puede dar los valores
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = "Toyota2"
    coche1._modelo = "Yaris2"  # Esto no es una buena practica
    coche1.__color = "Azul2"  # Ignoro la modificacion
    coche1._Coche__color = "Azul3"  # Es una mala practica
    coche1.conducir()
