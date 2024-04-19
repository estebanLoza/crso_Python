#Determinar si el numero ingresado por el usario es primo o no

#Son aquellos que son divisibles entre 1 y si mismos

num = int(input("Ingrese el numero: "))

cont = 1 #inicia
i =0 #iteracion

for cont in range(cont, num + 1):
    if num % cont == 0: #si esto es cierto entonces i incrementa 1 y como esta en 0
                        #si es cierto ahora valdra 1 
                        #y con eso vemos si es divisible entre 1 y entre si mismo(solamente)
        i+=1

if i > 2: #Estamos diciendo que tiene mas de 2 divisores y no solo entre 1 y si mismo
    print(f"El numero {num} NO es primo")
else:
    print(f"El numero {num} es primo")



