# Definir una lista de tipo str
nombres = ["Juan", "Karla", "Ricardo", "María"]
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de un a lista
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# Imprimir un rago
print(nombres[0:2])  # sin incluir el índice 2 (se resta 1)

# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
# Desde el índice indicado hasta el final
print(nombres[1:])
# Cambiar un valor
nombres[3] = "Ivone"
print(nombres)


# iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")

