#Funcionamiento de la sentencia break con for y while

for i in range(5):
    print(i)
    break #No llega el break

print('No llega el break por eso no funciona')

print('\n\n')

print('*****')

cadena = 'Python'

for letra in cadena:
    if letra == 'h':
        print('Se encontró la letra h')
        break
    # if letra == 'n':
    #     print("Se econtro la letra n") #Esto no viene en 'El libro de Python', sirve para entender el break
    print(letra) #Aquí si llega el break



print('\n\n')
print('*****')
print('Break con bucles While')

#*Break con bucles While

x = 5

while True:
    x -= 1    
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

print('\n\n')
print('*******')
print('Break  y bucles anidados')


#*Break y bucles anidados

for i in range(0, 4):
    for j in range(0, 4):
        break
        #Nunca se realiza más de una iteración
    #El break no afecta a este for
    print(i, j)
