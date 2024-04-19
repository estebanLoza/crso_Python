""""
Suma pares  e impares desde n hata m
 ejemplo del 4 al 10 o 5 a 11 y buscar sus pares y sumar los que haya en ese intervalo
"""

num1 = int(input("Ingrel pirmer intervalo: "))

num2 = int(input("Input ingrese el segundo intervalo: "))

suma = 0
sumaImpar = 0


while num1 <= num2:
    if num1 % 2 == 0:
        suma+=num1
    else:
        sumaImpar+=num1
    num1+=1

print(f'La suma PARES ES DE: {suma}')
print(f'La suma IMPAR ES DE : {sumaImpar}')