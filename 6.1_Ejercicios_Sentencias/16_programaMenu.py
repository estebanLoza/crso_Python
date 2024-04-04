""""
Hacer un menu que considere las siguientes opciones: 

1- Cubo de un numero
2 - Numero par o impar
3 - salir


"""""

import math #pARA USASR POTENCIAS

print("Seleccione una de las siguientes operaciones: ")
print("1)Cubo de un numero")
print("2)Numero par o impar")
print("3)Salir del programa")
op = int(input("Opcion: "))

if op == 1:
    numCubo = int(input("Escriba el numero para elevarlo al cubo: "))

    cubo = math.pow(numCubo,3)

    print(f"El numero {numCubo} al cubo es de {cubo}")
elif op == 2:
    numPar_Impar = int(input("Escriba el numero para saber si es par o impar: "))
    if numPar_Impar % 2 == 0:
        print("El numero es PAR")
    else:
        print("El numero es IMPAR")
elif op == 3:
    print("GRACIAS POR USAR EL PROGRAMA")
else:
    print("OPCION INVALIDA")
