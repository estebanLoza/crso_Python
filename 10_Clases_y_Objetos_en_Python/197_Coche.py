"""
Aqui esta es la continucación del archivo 196 sobre el 'encapsulamiento'

pero aqui veremos sobre el uso del get y set (dentro del mismo de encapsulamiento) que se usar cuando no estamos
dentro de la misma clase. Si no se usa en el 'programa principal'

get === acceder al valor

set == modificar el valor

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

    def get_marca(self):
        # accedemos al valor del atributo
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


# Programa principal

if __name__ == "__main__":
    # Creación de un primer coche
    coche1 = Coche("Toyota", "yaris", "azul")
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sea publicos
    # Aquí estamos ya modificando el atributo en vez de acceder
    coche1.set_marca("toyota2")
    coche1.set_modelo("yaris2")
    coche1.set_color("rojo")
    coche1.conducir()
