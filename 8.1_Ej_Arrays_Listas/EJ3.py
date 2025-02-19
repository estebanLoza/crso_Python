"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

"""

listaNumeros = []

count = 0

for numero in range(6):
    count += 1
    numeros = int(input(f"Escribe el {count} numero: "))
    listaNumeros.append(numeros)
listaNumeros.sort()

print(f"Los numeros mas grandes son {listaNumeros}")

