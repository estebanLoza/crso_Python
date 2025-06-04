# Este ejercicio es aplicando el encapuslamiento con los mismo datos de 193_EjercicioAritmetica


class Aritmetica:
    def __init__(self, operando1, operando2):
        self._operando1 = operando1  # Aqui hice a los 2 privados
        self._operando2 = operando2

    # Aqui no hay necesidad de usar el get por que esta dentro de la clase
    def sumar(self):
        suma = self.operando1 + self.operando2

        print(f"La suma es de {suma}")

    def restar(self):
        resta = self.operando1 - self.operando2
        print(f"La resta es de {resta}")

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    # opeando 2

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2


if __name__ == "__main__":
    print("**Ejemplo Clase airtmetico ***")
    aritmetica1 = Aritmetica(5, 7)

    print("Primer Objeto")
    print(f"Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}")
    print(f"Valor operando2 del objeto aritmetica1: {aritmetica1.operando2}")

    print("\n")

    aritmetica1.sumar()
    aritmetica1.restar()

    # segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print("\n")
    print("Segundo objeto")
    print("\n")
    print(f"Valor operando1 del objeto aritmetica2: {aritmetica2.operando1}")
    print(f"Valor operando2 del objeto aritmetica2: {aritmetica2.operando2}")
    print("\n")
    aritmetica2.sumar()
    aritmetica2.restar()
