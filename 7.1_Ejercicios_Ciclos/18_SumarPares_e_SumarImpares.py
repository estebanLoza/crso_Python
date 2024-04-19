""""
Sumar un numero y restar el siguiente 1-2+3-4+5-6+7

Impares == Positivos
Pares == Negativos

"""""

numeros = int(input("Ingresa hasta que numer: "))

sumaPares = 0
sumaImpares = 0

contador = 0

while contador <= numeros:
    if contador % 2 ==0:
        sumaPares+=contador
    else:
        sumaImpares+=contador
    contador += 1

sumaGeneral = sumaImpares - sumaPares

print(f'La suma/resta hasta el {numeros} es de {sumaGeneral}')
