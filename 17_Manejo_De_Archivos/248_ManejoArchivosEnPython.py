##Esto es para el manejo y abrir archivos en python
#En pdf


#Aquí se creó el archivo prueba, como no existe (al principio) se creó
#w es de escribir en ese archivo


# try:
#     archivo = open('prueba.txt', 'w')
# except Exception as e:
#     print(e)
# finally:
#     archivo.close()
#




try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregamos información al archivo')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
