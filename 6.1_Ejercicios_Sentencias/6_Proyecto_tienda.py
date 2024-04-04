
""""
Proyecto de un cajero automatico con un saldo de 3000
"""

saldo = 3000

print("****Bienvenido al Proyeco tienda/Cajero*****")
print("Seleccione una de las Siguientes Operaciones: ")
print("1)Agregar Saldo")
print("2)Retirar")
print("3)Salir de la Caja")

op = int(input("Opcion: "))

if op == 1:
    
    agregar = int(input("Ingrese la cantidad: "))
    suma = saldo + agregar
    print(f"Su saldo ahora es de {suma}")

elif op == 2:

    retirar = None
    resta = None  #Decimos que estas dos no tienen un valor 


    retirar = int(input("Ingrese la cantidad de retiro: "))
    if retirar > saldo:  
        #Daremos la opcion de que si el cliente se equivoca con el retiro pueda volver escribir la cantidad
        # de retiro y hacer la operacion, pero si la escribe bien, se hace directo la operacion

        print(f"Su retiro excede a su saldo, saldo actual {saldo}")

        retirar = int(input("Vuelve a escribir otra cantidad menor a esta: "))
        
        resta = saldo - retirar

        print(f"Su saldo ahora es de {resta}")
    else:
        resta = saldo - retirar
        print(f"Su saldo ahora es de {resta}")

elif op == 3:
    print("Gracias por su visita")

else:
    print("Opcion invalida, seleccione una de las 3")


    
    