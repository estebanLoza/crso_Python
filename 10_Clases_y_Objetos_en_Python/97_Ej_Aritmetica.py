#SE CREA UN PARA HACER OPERACION ARITMETICOS DE SUMA, RESTA, MULTIPLICACION
#EN PROGRAMACIÓN ORIENTADA A OBJETOS

class Aritmetica:
    """
        clase Aritmetica para hacer las operaciones de sumar, restar, multipplicar y dividir
    """ 
    def __init__(self, OperandoA, OperandoB):
        self.operandoA = OperandoA
        self.operandoB = OperandoB

    def sumar(self):

        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA  - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB
    
    def division(self):
        return self.operandoA / self.operandoB




Aritmetica1 = Aritmetica(5, 6)

print(f"Suma: {Aritmetica1.sumar()}")
print(f"Resta: {Aritmetica1.restar()}")
print(f"Multiplicacion: {Aritmetica1.multiplicacion()}")
print(f"Dividir: {Aritmetica1.division(): .2f}") #aqui indicamos cuantos numeros queremos mostrar despues del punto

