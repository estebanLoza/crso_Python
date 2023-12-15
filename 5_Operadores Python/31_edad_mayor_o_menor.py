#Determina si la edad es mayor o menor

edad = int(input('Escribe tu edad: '))

if edad >= 18:
    print('Eres mayor de Edad')
else:
    print('No eres mayor de Edad')


#segunda manera de hacerlo

edadMayor = 18

edadPersona = int(input('Escribe tu edad: '))

if edadPersona >= edadMayor:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')