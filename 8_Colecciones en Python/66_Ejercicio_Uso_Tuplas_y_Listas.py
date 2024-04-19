#Dado la siguiente tupla,
# crear una lista que solo incluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)

#Declaramos la lista

lista = []

#Filtramos los elementos menores a 5 de la tupla

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento) #? append es agregar, estamos agregando elemento en lista

print(lista)
