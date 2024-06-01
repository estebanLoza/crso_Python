
""""
Hacer un programa que pida por pantalla un numero del 1 al 10 y mediante un procedimiento muestre por pantalla el numero
escrito en letras
"""

global numero #Declaro esta variable global

def nombreNumeros():  ## Declracion de la sentencia if para que se imprima el valor del numero y ademas la declracion
                        ## De la funcion desde arriba.
    
    if numero == 1:
        print("Uno")
    elif numero == 2:
        print("Dos")
    elif numero == 3:
        print("Tres")
    elif numero == 4:
        print("Cuatro")
    elif numero == 5:
        print("Cinco")
    elif numero == 6:
        print("Seis")
    elif numero == 7:
        print("Siete")
    elif numero == 8:
        print("Ocho")
    elif numero == 9:
        print("Nueve")
    elif numero == 10:
        print("Diez")


numero = int(input("Ingrese un numero: "))  #Se pide el numero 

while numero < 1 or numero > 10: #Este bucle se imprimira hasta que este dentro de ese rango de 1 a 10
                                #NO es necesario poner un contador o break solo se rompera cuando se cumple la sentencia
    numero = int(input("Ingresa un NUMERO: "))
    
nombreNumeros() #LLamamos la funcion cuando se cumplen las otras dos arriba.
                #*RECUERDA que el codigo se lee de arriba hacia abajo.
