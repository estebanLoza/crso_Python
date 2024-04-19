"""

    Determinar si un numero es primo (Hasta el digito que ponga el usuario)

    Numero Primo == Solo divisible entre 1 y entre si mismo

    Ej = 2 3 5 7 11 13 numeros primos 


        *****CON CICLO FOR****


"""

num = int(input("Ingrese el numero: "))

cont = 1 #inicia
i =0 #iteracion

for cont in range(cont, num + 1):
    if num % cont == 0: #si esto es cierto entonces i incrementa 1 y como esta en 0
                        #si es cierto ahora valdra 1 
                        #y con eso vemos si es divisible entre 1 y entre si mismo
        i+=1

if i > 2:
    print(f"El numero {num} NO es primo")
else:
    print(f"El numero {num} es primo")




