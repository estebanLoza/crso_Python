""""
Determinar todos los multiplos de 5 de 1 hasta n

ej
 *Usuario escribe hasta 10
  === 5 y 10

"""


numero = int(input("Escribe hasta que numero: "))

cont = 1

for cont in range(cont, numero + 1): # el + 1 en el range se refiere que se sumara en 1 en 1 hasta llegar al numero que el usuario escribio
    if cont % 5 == 0 :
        print(f"{cont} es multiplo de 5")

