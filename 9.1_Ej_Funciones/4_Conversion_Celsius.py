#Convertir los grados Celsius a Fahrenheit
#y de Celsius a Kelvin y que cada vez que se termina vuelva a iniciar y con un menu de 3 opciones
#donde la 3 sea la salida

celsius = 0



def grand_Kelvin( kelvin):
    conversion = kelvin + 273.15
    print(f"El valor de la conversion es de {conversion}")
    return conversion


def grand_Fahren( fahren ):
    conver_Fahren = ( fahren * (9/5)) + 32 
    print(f"La conversion es de {conver_Fahren}")
    return conver_Fahren

def menu():
    print("1)Convertir a Kelvin")
    print("2)Convertir a Fahrenheit")
    print("3)Salir")
    op = int(input("Opcion: "))
    
    if op == 1:
        grand_Kelvin(celsius)
    elif op == 2:
        grand_Fahren(celsius)
    elif op ==3: 
        print("Gracias por usar el programa")
    else:
        print("Opcion invalida")



print("***Bienvenido al programa***")
celsius = float(input("Ingrese los grados Celsius: "))

menu()
