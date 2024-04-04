"""
En este ejercicio se le pidira al usuario los siguientes datos de un libro

1- Nombre del libro
2- Id del libro
3- Precio del libro (con decimales)
4- Si el envio es gratis o no (con respuesta booleana)
"""


print("Proporcione los siguientes datos del libro: ")

nombre = input("Proporciona el nomber: ")

id = int(input("Proporcione el ID: "))

precio = float(input("Proporcione el precio: "))

envio = input("Indica si el envio es gratuito (True/False): ")

if envio == "True":
    envio = True
elif envio == "False":
    envio == False
else:
    envio = print("Valor incorrecto debe ser True/False")

print(f"Nombre {nombre}")

print(f"Id: {id}")

print(f"Precio: {precio}")

print(f"Envio Gratuito?: {envio}")




