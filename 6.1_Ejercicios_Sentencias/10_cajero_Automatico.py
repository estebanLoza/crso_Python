"""
Hacer un programa que simule un cajero automatico con un
saldo inicial de 1000 dolares
"""

saldoInicial = 1000

print("Bienvenido al Programa de un Cajero Automatico")
print("Seleccione una de las siguientes opcinoes: ")
print("1)Agregar saldo")
print("2)Retirar Dinero")
print("3)Consultar Saldo")
print("4)Salir")

opcion = int(input("Opcion: "))

if opcion == 1:
    agregarSaldo = int(input("Escriba la cantidad que va a agregar: "))
    suma = agregarSaldo + saldoInicial
    print(f"Ahora el saldo es de {suma}")
elif opcion == 2:
    retirarSaldo = int(input("Agrega la cantidad que va a retirar: "))
    if retirarSaldo > saldoInicial:
        print(f"Su retiro excede su saldo de {saldoInicial}")
    else:
        resta = saldoInicial - retirarSaldo
        print(f"Su saldo ahora es de {resta}")
elif opcion ==3:
    print(f"Su saldo es de {saldoInicial}")
elif opcion == 4:
    print("Gracias por usar el programa")
else:
    print("Eliga una opcion del 1 al 4")