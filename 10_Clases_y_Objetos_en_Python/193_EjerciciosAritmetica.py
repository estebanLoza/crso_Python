# Este ejercicio abarca hasta el 195


class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        suma = self.operando1 + self.operando2

        print(f"La suma es de {suma}")

    def restar(self):
        resta = self.operando1 - self.operando2
        print(f"La resta es de {resta}")


if __name__ == "__main__":
    print("**Ejemplo Clase airtmetico ***")
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()

    # segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
