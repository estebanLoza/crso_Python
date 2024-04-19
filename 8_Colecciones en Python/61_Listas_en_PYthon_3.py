# Definir una lista de tipo str
nombres = ['Juan','Karla','Ricardo', 'María']

# preguntar el largo de una lista
print(len(nombres))

# agregar un elemento
nombres.append('Lorenzo')
print(nombres)

# insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)

# remover un elemento
nombres.remove('Octavio')
print(nombres)

# remover el último valor agregado
nombres.pop()
print(nombres)

# eliminar un indice
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# borrar la lista por completo
del nombres
print(nombres)
