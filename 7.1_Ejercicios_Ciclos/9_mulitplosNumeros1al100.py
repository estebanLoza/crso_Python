""""
/*Escribir los multiplos de 1 hasta el 100 de 2, 3, 4, 5 y 7*/
 al numero que digite el usario
"""""


op = int(input("Escribe el numero para saber sus multiplos del 1 al 100: "))

i = 1

for i in range(i, 100 + 1):
    if(i%op==0):
        print(f"{i} es muliplo del {op}")
    