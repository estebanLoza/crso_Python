#con with evitamos el usar el close


with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())
