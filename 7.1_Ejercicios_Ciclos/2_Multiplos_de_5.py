""""
Determinar todos los multiplos de 5 de 1 hasta n

ej
 *Usuario escribe hasta 10
  === 5 y 10

"""


numero = int(input("Escribe hasta que numero: "))

cont = 1

for cont in range(cont, numero + 1):
    if cont % 5 ==0 :
        print(f"{cont} es multiplo de 5")

