""""
Hacer un programa que muestre un menu con las opciones sumar, restar, multiplicar y dividr,
el programa debe solicitar una opcion y realizar la tarea elegida, se debe usar un procedimiento

"""

def suma():
    num1 = float(input("Ingrese el numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    operacion = num1 + num2
    print(f"El valor de la Suma {operacion}")
    print("Que mas?")

def resta():
    num1 = float(input("Ingrese el numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    operacion = num1 - num2
    print(f"El valor de la resta es de {operacion}")
    print("Que mas?")


def multi():
    num1 = float(input("Ingrese el numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    operacion = num1 * num2
    print(f"El valor de la multiplicacion es de {operacion}")
    print("Que mas?")


def dividir():
    num1 = float(input("Ingrese el numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    operacion = num1 / num2
    print(f"El valor de la division es de {operacion}")
    print("Que mas?")



def menu():
    while True: #!Esto sirve como si fuera un do-while de c donde se creara un bucle para que pueda seguir
                #!se detengra cuando marcamos 5 que es la salida 
        print("1)Sumar\n2)Restar\n3)Multiplicar\n4)Dividir\n5)Salir")
        op = int(input("Opcion: "))

        
        if op == 1:
            suma()
        elif op == 2:
            resta()
        elif op == 3:
            multi()
        elif op == 4:
            dividir()
        elif op == 5:
            print("Gracias por usar el progrma.")
            break #!Aqio se termina el bucle de while al momento de presionar 5
        else:
            print("\t*****OPCION INVALIDA******")



menu()