"""
Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.
"""


numeros = []


for numero in range(10):
    numero = int(input(": "))
    numeros.append(numero)



#Invierte los numeros de la lista
numeros.sort(reverse=True)

#OPCION2: numero.reverse()


#Itera los numeros sin la aparencia de lista y el en es para que sea con , y espacio
for n in numeros:
    print(n, end=", ")