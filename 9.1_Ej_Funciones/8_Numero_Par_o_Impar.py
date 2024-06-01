#Determinar si un numero es par o no

def par():
    if numero % 2 == 0:
        print("Es par")
    else:
        print("IMPAR")

numero = int(input("Ingresa un numero: "))

par()