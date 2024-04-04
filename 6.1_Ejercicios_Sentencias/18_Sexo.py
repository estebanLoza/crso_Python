""""
Ingresar por teclado el nombre, la edad y el sexo de
cualquier persona e imprima, solo si la persona es de sexo femenino
y mayor de edad ,el nombre de la persona 


"""
#Usario ingresa datos

nombre = input("Ingrese su nombre: ")

edad = int(input("Ingrese su edad: "))

sexo = input("Ingres su sexo: ")

#que no imparte si es mayusculas o minusculas 

sexo = sexo.lower()

if sexo == "femenino" and edad >= 18: 
    print(f"Su nombre es {nombre}")
else:
    print("Lo siento no cumple con los requisitos")