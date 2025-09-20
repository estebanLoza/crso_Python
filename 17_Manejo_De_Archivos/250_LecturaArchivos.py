archivo = open('pruebaDos.txt', 'r', encoding='utf8')

#Esto lee todos los caracteres

# print(archivo.read())



#Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))
#
#Leer lineas completas
# print(archivo.readline())
# print(archivo.readline())


#Iterar el archivo
# for linea in archivo:
#     print(linea)

#Acceder a una linea de la lista

# print(archivo.readlines()[1])

#Podemos copiar un archivo para crear uno original
#abrimos un nuevo archivo
#a - anexar información

archivo2 = open('copia.txt', 'a', encoding='utf8')

archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proceso de leer y copiar el archivo ')
