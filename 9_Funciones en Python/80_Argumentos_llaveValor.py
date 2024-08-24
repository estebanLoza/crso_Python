#*Key words

#** Argumentos Variables

"""
En python, los argumentos variables permiten que una función acepte un número arbitario de elementos. Hay dos tipos principales

    1-. Argumentos posicionales vairbles "*args": Permite pasar múltiples argumentos posicionales a una función, recibiéndolos
    como una tupla dentro de la función

    2-. Argumentos con Palabra clave **kwargs: Recibe los argumentos en forma de diccionario (llave-valor o key-value)

"""


print("**EJEMPLO 1")
def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f"{llave}: {valor}")

listarTerminos(IDE="Integrated Developement Evironment", PK="Primary Key")
listarTerminos(DBMS="Database Management System")

#!NOTA PARA LAS KEYWORDS SE TIENE QUE IGUALAR "=", PARA QUE LA FUNCIÓN LO TOME COM KEYWORDS

print("")
print("")
print("**EJEMPLO 2")

def sueperHeroe_superPoderes(nombre, *args, **kwargs):
    print(f"Superheroe:{nombre} - {args} - Mas info: {kwargs}")


#Llamar la función

sueperHeroe_superPoderes("Spiderman", "Instinto Arácnido", edad=17, empresa="Marvel")
sueperHeroe_superPoderes("ironMan", "Instinto Artificial", "PlayBoy", "Millonario", edad=37, empresa="Industries Stark", traje="Armadura de Hierro")
