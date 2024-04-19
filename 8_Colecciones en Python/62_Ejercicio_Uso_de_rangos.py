# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1


ejercicio1 = 0

for ejercicio1 in range(ejercicio1, 10 + 1):
    if ejercicio1 % 3 == 0:
        print(ejercicio1)

print('Rango con valores de inicio y fin')

ejercicio2 = 2

for ejercicio2 in range(ejercicio2, 6 + 1):
    print(ejercicio2)

#manera dos
print('\n')

rango = range(2,6 + 1)

for ejercicio2 in rango:
    print(ejercicio2)

print('Rango con valores de inicio, fin y salto')

ejercicio3 = 3

while ejercicio3 <= 10:
    print(ejercicio3)
    ejercicio3 += 2

