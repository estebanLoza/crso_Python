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

    def multiplicar(self):
        multiplicar = self.operando1 * self.operando2
        print(f"La multiplicacion es de {multiplicar}")


# Código principal (para la cración y demostración de los objetos)
if __name__ == "__main__":
    print("**Ejemplo Clase airtmetico ***")
    aritmetica1 = Aritmetica(5, 7)  # primer objeto
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()

    print("\n")

    # segundo objeto
    print("Segundo objeto")
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
