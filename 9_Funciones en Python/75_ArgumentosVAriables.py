#** Argumentos Variables

"""
En python, los argumentos variables permiten que una función acepte un número arbitario de elementos. Hay dos tipos principales

    1-. Argumentos posicionales vairbles "*args": Permite pasar múltiples argumentos posicionales a una función, recibiéndolos
    como una tupla dentro de la función

    2-. Argumentos con Palabra clave **kwargs: Recibe los argumentos en forma de diccionario (llave-valor o key-value)

"""


print("***Argumentos Variables **")

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f"Super hereoe: {superheroe} - {nombre} - {args}")


#Llamamos la función

superheroe_superpoderes("Spiderman", "Peter Parker", "Instinto Arácnido", "Telaraña")


#salida
#***Argumentos Variables **
#Super hereoe: Spiderman - Peter Parker - ('Instinto Arácnido', 'Telaraña')
                                                    #**esto son los argumentos

#!NOTA: LOS ARGUMENTOS SIMPRE VAN AL FINAL, PORQUE SINO EL PROGRMA NO LEEARA LOS DEMAS EJEMPLO: 

#def superheroe_superpoderes(*args, superheroe,nombre):
  #  print(f"Super hereoe:{args}- {superheroe} - {nombre}")


#Llamamos la función

#superheroe_superpoderes("Spiderman", "Peter Parker", "Instinto Arácnido", "Telaraña") #solo cambia los parametros (instinto aracnido y teleraña)

#y no funcionará