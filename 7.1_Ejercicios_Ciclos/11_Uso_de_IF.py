"""
Digite un numero, si el numero supera a 10,
multiplique los 10 primeros numeros.
y si no sumelos
"""

primeroDiez = int(input("Ingrese el numero: "))

cont = 1 #como se multiplica para mayor a 10 se inicia en 1
multi = 1 #Como se va a guardar ahi del 1 al 10 y se multiplica tambien se inicia en 1
sum = 0 #como no se multiplica es 0 para que no varie en la suma
if primeroDiez > 10:
    for cont in range(cont, 10+ 1):
        multi*=cont

    print(f"La multiplicacion es de {multi}")
else:
    for cont in range(cont, 10 +1):
        sum+=cont
    print(f"La suma es de {sum}")
