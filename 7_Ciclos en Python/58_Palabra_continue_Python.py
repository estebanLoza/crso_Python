'''
La diferencia entre el break y continue es que el continue no rompe el bucle, 
si no que pasa a la siguiente iteración saltando el código pendiente.
'''


cadena = 'Python'

for letra in cadena:
    if letra == 'P':
        continue
    # x = 2 + 2
    # print(x)  esto no viene en 'El libro de Python', solo es un ejemplo para ver como es que funciona el continue
    print(letra)



print('\n\n')
print('*****')
print('Ejemplo 2')

x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)
print('Vemos que el 3 no esta dado que continue aun a verlo encontrado')