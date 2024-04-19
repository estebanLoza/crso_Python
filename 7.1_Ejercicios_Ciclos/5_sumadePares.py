
""""
/*
Suma de 20 numeros pares 20

    2 4  6 8 10 asi hasta 20 numeros


*/
"""""

num = 40 # Hasta 40 es la posicion 20 de los numeros pares
cont = 1
sumaPares = 0
while cont <= num:
    if cont % 2 == 0:
        print(f"{cont} es par")
        sumaPares += cont 

    cont += 1
print(f"La suma total de los 20 pares es de {sumaPares}")



print("\n")

print("****CON CLICO FOR*****")


numero = 40
cont = 1
suma = 0

for cont in range(cont, numero + 1):
    if cont % 2 == 0:
        print(f"{cont} es par")
        suma+=cont

print(f"La suma total de los 20 pares es de {suma}")


