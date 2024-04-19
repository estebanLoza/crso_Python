""""
Suma pares  e impares desde n hata m
ejemplo del 4 al 10 o 5 a 11 y buscar sus pares 
y sumar los que haya en ese intervalo
Y DIGA CUANTOS NUMEROS HAY (PARES)

"""""


num1 = int(input("Ingrese el primer intervalo: "))

num2 = int(input("Ingrese el segundo intervalo: "))

suma = 0
sumaImpares = 0
IndicadorNuemeroPar = 0
IndicadorNumImpar = 0

while num1 <= num2:
    if (num1 % 2 == 0):
        suma+=num1
        IndicadorNuemeroPar+=1 #Nos dice cuantos pares hay
        print(f"{num1} es par")
    else:
        sumaImpares+=num1
        IndicadorNumImpar+=1 #Nos dice cuanto impares hay
    num1+=1 #para que sentencia se cumpla y no crea un bucle

print(f"La suma total PAR es de {suma}")
print(f"La cantidad de PARES ES DE {IndicadorNuemeroPar}")


print(f"La suma total IMPAR es de {sumaImpares}")
print(f"La cantidad de IMPAR ES DE {IndicadorNumImpar}")