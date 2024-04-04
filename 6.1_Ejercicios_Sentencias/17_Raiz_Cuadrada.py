"""
/*
    Ingrse un numero y calcule e imprima su raiz cuadrada.
    Si el numero es
    negativo imprima el numero y un mensaje que diga tiene
    raiz imaginaria
*/


"""

import math

numero = float(input("Escriba el numero para la raiz cuadrada: "))

if numero < 0:
    print(f"El numero {numero} tiene raiz imaginaria (i)")
else:
    raiz = math.sqrt(numero)

    print(f"La raiz cuadrada de {numero} es de {round(raiz,2)}")

