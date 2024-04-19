""""
Determinar suma de todos los numeros hasta el numero que de el usuario

Ej
    Escribe el numero: 5

    1+2+3+4+5 = 15

"""

numero = int(input("Ingrese el numero que quiere que sea hagas la suma: "))

cont = 0
suma = 0 #No guarde basura y se ejecute bien

while cont <= numero:
    suma+=cont
    cont+=1
print(f"La suma total hasta el numero {numero} es de {suma}")


print("\n")
print("\n")
print("\n")

print("*****INTENTO CON FOR*******")


num = int(input("ingrese el numero: "))

contador = 0
sum = 0

for contador in range(contador, num + 1):  
    sum += contador;
    
print(f"La suma total hasta el numero {num} es de {sum}")
