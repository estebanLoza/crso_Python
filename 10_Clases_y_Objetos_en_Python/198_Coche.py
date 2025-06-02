""" "
Esto es la continuación del ejercicio 197

donde se aplicará las mejores practicas de python


get == @property

set == (atributNombre).setter

"""


class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo
        #     self.__color = color  # Atributo privado
        self._color = color

    def conducir(self):
        print(
            f"""Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        """
        )

    #    def get_marca(self):
    # accedemos al valor del atributo
    #       return self._marca

    @property
    # con property estamos indicando que este atributo es una propiedad de nuestra clase, el por eso que
    # comentamos el def de arriba
    def marca(self):
        return self._marca  # lo escribimos como esta arriba en __init__

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal

if __name__ == "__main__":
    # Creación de un primer coche
    coche1 = Coche("Toyota", "yaris", "azul")
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sea publicos
    # Aquí estamos ya modificando el atributo en vez de acceder

    #    coche1.set_marca("toyota2")
    #   coche1.set_modelo("yaris2")
    #  coche1.set_color("rojo")
    # coche1.conducir()

    # Aquimandamos a simplificar
    # Atriubto de la marca del coche 1
    print(
        f"Atributo marca coche1: {coche1.marca}"
    )  # de manera indirecta accede al atributo de protegido

    # modificamos el nombre
    coche1.marca = "toyota3"
    coche1.modelo = "mustang"
    coche1.color = "elfuerte"
    print(
        f"Atributo de la marca es de {coche1.marca}"
    )  # como si fuera un atributo publico pero no lo es es portegido
    print(f"Atriubto del modelo es de {coche1.modelo}")
    print(f"Atributo del color es de {coche1.color}")
