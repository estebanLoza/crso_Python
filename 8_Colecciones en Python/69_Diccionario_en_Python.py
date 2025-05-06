# Creamos el diccionario inicial del escritor
escritor = {
    "nombre": "Gabriel García Márquez",
    "edad": 87,
    "libros": ["Cien años de soledad", "El amor en los tiempos del cólera"]
}

# Mostramos los datos actuales
print("Datos del escritor:")
for clave, valor in escritor.items():
    print(f"{clave}: {valor}")

print("\nAhora agregaremos la nacionalidad del escritor.")

# Solicitamos al usuario que ingrese la nacionalidad
nacionalidad = input("Ingrese la nacionalidad del escritor: ")

# Agregamos la nueva clave al diccionario
escritor["nacionalidad"] = nacionalidad  #----> este es el values

# Mostramos el diccionario actualizado
print("\nDatos actualizados del escritor:")
for clave, valor in escritor.items():
    print(f"{clave}: {valor}")


print("\nAhora agregamos si se caso o no.")

matrimonio = input("Ingrese el nombre de su pareja: ")

escritor["pareja"] = matrimonio

print("\n Datos actualizados del escritor: ")
for clave, valor in escritor.items():
    print(f"{clave}: {valor}")



