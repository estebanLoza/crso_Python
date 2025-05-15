"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

inforPersona =  {}


nombre = input("Ingrese el nombre: ")

edad = int(input("Ingrese su edad: "))

direccion = input("Ingrese su direccion: ")

telefono = int(input("Ingrese el telefono: "))

inforPersona["nombre"] = nombre
inforPersona["edad"] = edad
inforPersona["direccion"] = direccion
inforPersona["telefono"] = telefono


#   Probar que sirve la forma que lo puse
#for laInfo in inforPersona.items():
#       print(f"{laInfo}")
#

print(f"{nombre} tiene {edad} años, vive en {direccion}, y su numero de telefono es {telefono}")


