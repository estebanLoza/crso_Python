""""
Programa que borra la pantalla al presionar 1

"""""
import os #Libreria del sistema como stdlib en C

print(f"*******PROGRAMA QUE BORRA LA PANTALLA ******")
print(f"\t***ESCIBRE EL NUMERO******")

numero = int(input(f"Ingrese el numero para borrar la pantalla: "))

if numero == 1:
    os.system("cls") #Para que pueda usar cls y limpie el mensaje de arriba
    print(f"Borrarste la pantalla")
else:
    print(f"Ese no es el numero")
    numero = int(input(f"Vuelve a escribir el numero 1: "))

    if numero == 1:
        os.system("cls")  #NOTA: NO PUEDES USAR clear, como en la terminal windows/linux comand 30/03/2024
        print(f"Borraste la pantalla")