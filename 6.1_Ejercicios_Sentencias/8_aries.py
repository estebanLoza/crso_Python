""""
Pedirle al usario que digite su nombre y signo
e imprimir su nombre si su signo es aries.
"""""

nombre = input("Ingrese su nombre: ")

signo = input("Escriba su signo: ")

if signo == "aries" or signo == "Aries" or signo == "ARIES":
    print(f"su nombre es {nombre}")
else:
    print("Su signo no es Aries")


##Otra manera es que pongamos el comando "nombreVariable.lower()"
    
print("\n")

print("Segunda manera con el comando .lower()")
    
nombre = input("Ingrese su nombe: ")

signo = input("Escriba su signo: ")


signo = signo.lower() #Con esto el programa será insensible a mayusculas en el ingreso del singo
                    #Para que este comando funcione debes declarar las letras con "" y minusculas


if signo == "aries":
    print(f"su nombre es {nombre}")
else:
    print("Su signo no es Aries")

    
