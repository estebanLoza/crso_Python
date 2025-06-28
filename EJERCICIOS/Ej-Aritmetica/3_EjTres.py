"""
Escribir un programa que lea un entero positivo, n,
introducido por el usuario y después muestre en pantalla la suma de
todos los enteros desde 1 hasta n.La suma de los n primeros enteros positivos
puede ser calculada de la siguiente forma:

    suma = n(n+1)/2

"""


n = int(input("Introduce el numero: "))

suma = n*(n+1)/2

print(f"La suma del 1 hasta {n} es de {suma}")
