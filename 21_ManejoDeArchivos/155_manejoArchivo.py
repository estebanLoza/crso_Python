#Veremos como trabajar archivos tipos textos
try: 
    archivo = open(".texto.txt", "w") #si no existe lo crea
    #para agregar informacion a ese archivo
    archivo.write("Agregamos informacion al archivo")
    archivo.write("Adios Perro")
    
except Exception as e:
    print(e)
finally:
    archivo.close()