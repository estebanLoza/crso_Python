# Este ejercicio abarca hasta el 195


class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        suma = self.operando1 + self.operando2

        print(f"La suma es de {suma}")


if __name__ == "__main__":
    opSuma = Aritmetica(10, 10)
    opSuma.sumar()
