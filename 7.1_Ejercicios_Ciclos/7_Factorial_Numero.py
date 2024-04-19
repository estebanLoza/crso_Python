""""
//Calcular el factorial de un numero dado por el usario
// 5! -> 5*4*3*2*1 == 120
// 4! -> 4*3*2*1
// 3! -> 3*2*1
// 2! -> 2*1

"""""


num = int(input("Ingrese el numero para hacer Factorial: "))

cont = 1 #El comun de todos los factoriales inicio y contador

factorial = 1 #Varible o declaracion, es donde se va a guardar todas las multiplicaciones 
                #Si la iniciamos en 0, pues al momento de guardar y hacer la operacion (*)
                #siempre dara 0

#*****FOR*****

# for cont in range(cont, num + 1):
#     factorial *= cont

#****WHILE****

while cont <= num:
    factorial*=cont
    cont += 1
    print(f"{factorial} con while") #arroge el valor de la multiplicacion que se vaya guardando



print(f"El factorial del numero {num} es de {factorial}")