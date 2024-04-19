#Suma de los n primeros numeros
# 5, 1 + 2 + 3 +4 + 5 = 15

cantidad = int (input("Ingrese hasta que numero hacer suma: "))

cont = 0
suma = 0

while cont <= cantidad:
    suma+=cont
    cont+=1

print(f"La cantidad total hasta el {cantidad} es de { suma}")

print("\n Con ciclo for")


# contador = 0
# sum = 0

        ##PROBANDO SI PUEDO PONERLO COMO EN FOR EN C <= O >=


# if contador < cantidad + 1:
#     for contador in range(contador, cantidad + 1):
#         sum+=contador

# print(f"La suma es de {sum}")