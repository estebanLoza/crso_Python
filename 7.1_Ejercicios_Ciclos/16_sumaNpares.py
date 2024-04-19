"""
Hacer un programa que imprima la suma de todos los numeros
pares que hay desde 1 hasta n, y diga cuantos numeros hay
"""""

inicio = int(input("Ingrese hasta que numero: "))

contador = 1
suma  = 0
indiPar = 0
for contador in range(contador, inicio + 1):
    if contador % 2 ==0:
        suma+=contador
        indiPar+=1
        print(f'{contador} es par')
print(f'La suma total de pares es de {suma}')
print(f'La cantidad de pares que hay es de {indiPar}')