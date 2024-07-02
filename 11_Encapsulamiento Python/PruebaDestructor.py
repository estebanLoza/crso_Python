from Destructor import Persona


print("Creacion de Objetos".center(50, "-"))  #Estamos indicando que va a tener 50 caracteres
persona1 = Persona("Karla", "Gomez", 30)
persona1.mostrar_detalle()


print("Eliminacion objetos".center(30,"-"))
del persona1


