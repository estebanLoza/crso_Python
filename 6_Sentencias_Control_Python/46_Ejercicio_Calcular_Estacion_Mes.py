"""

EJERCICIO Calcular La Estación según el Mes proporcionado


"""
estacion = None  # que esta declaracion no tiene un valor fijo/no contiene y su valor va a variar

estacion = int(input("Ingrese el numero del mes: "))


if estacion == 1 or estacion == 2 or estacion == 12:
    print(f"La estacion del año es Invierno en el mes {estacion}")

elif estacion == 3 or estacion == 4 or estacion == 5:
    print(f"La estacion es la primavera en el mes {estacion}")

elif estacion == 6 or estacion == 7 or estacion == 8:
    print(f"La estacion es el Verano en el mes {estacion}")

elif estacion == 9 or estacion == 10 or estacion == 11:
    print(f"La estacion es otoño en el mes {estacion}")

else:
    print("El mes no existe")


# MANERA 2 DEL VIDEO


# if estacion == 1 or estacion ==2 or estacion == 12:

# elif estacion == 3 or estacion == 4 or estacion == 5:
#

# elif estacion == 6 or estacion == 7 or estacion == 8:
#

# elif estacion == 9 or estacion == 10 or estacion == 11:
#

# else:
#     print("El mes no existe")

# print(f"Para el mes {mes} la estacion es: {estacion}")
