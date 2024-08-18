"""
Calcula el Area de un triangulo


"""


nombre = input("Ingresa tu nombre: ")

print("Hola " + nombre + " este programa calcula el Area de un triangulo y el area de un cuadrado")

base = int(input("Ingresa la base: "))

altura = int(input("Ingresa la altura: "))


area = (base * altura) / 2


print(f"El area del triangulo es de {round(area,2)}") #round sirve para redondear a 2 decimales

print("Ahora sigue el area de un cuadrado")

lado = int(input("Ingrese el lado del cuadrado: "))


area = pow(lado,2) #sirve para calcular una pontencia

print(f"El area de un cuadrado es de {area}")
