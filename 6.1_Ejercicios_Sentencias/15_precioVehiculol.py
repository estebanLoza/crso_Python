""""
Seleccionar un tipo de vehiculo e indicar el peaje a pagar
segun un valor numerico

1 - turismo, peaje = 500
2 - autobus, peaje == 3000
3 - motocicleta, peaje = 300
caso contrario - Vehiculo no autorizado

"""


print("Seleccione el vehiculo que utiliza")
print("1)Turismo")
print("2)Autobus")
print("3)Motocicleta")
op = int(input("Opcion"))


if op == 1:
    print(f"El peaje a pagar es de 500")
elif op == 2:
    print(f"El peaje a pagar es de 3000")
elif op == 3:
    print(f"El peaje a pagar es de 300")
else:
    print(f"Vehiculo no autorizado")