"""
Sacar la hipotenusa de un triangulo Rectangulo
pidiendo al usuario el valor de los 2 catetos

"""


import math


cateto1 = float(input("Escribe el Primer Cateto: "))
cateto2 = float(input("Escribe el Segundo Cateto: "))


hipotenusa = math.sqrt((math.pow(cateto1,2) + math.pow(cateto2,2)))

print(f"La hipotenusa del triangulo Rectangulo es {round(hipotenusa,2)}")

