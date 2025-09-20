##Aquí vemos como hacer para el uso de caracteres en los textos en los archivos
#Por ejemplo como el acento



try:
    archivoDos = open('pruebaDos.txt', 'w', encoding='utf8') #Agregamos el enconding para soporte de Caracteres
    archivoDos.write('Agregamos información al archivo\n')
    archivoDos.write('Adios')
except Exception as e:
    print(e)
finally:
    archivoDos.close()
    print('Fin del archivo')
  
