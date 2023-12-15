#DETERMINA SI EL NUMERO ES IMPAR O PAR

a = int(input('Escribe el numero: '))

#estamos preguntado que si al momento de dividir a entre 2 su residuo es igual a 0 es par

if a % 2 == 0:
    print(f'El numero {a} es par')
else:
    print(f'El numero {a} es impar')

