##Clase Object
##Esto es de los videos del 220 al 221


"""
   Si no especificamos en donde herademos la clase o algo.
   De manera indirecta se hereda de la clase Object.


    



"""


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    #Sobreescribir el metodo __str__ 
    def __str__(self):
        return f''' Persona:
            nombre = {self.nombre}
            apellido = {self.apellido}
            Dir. mem.   {super.__str__(self)}
        '''
    ##Si no hubieramos sobrescribimos el str lo que se hace
    ##Es que se imprime la memoria del objeto


#Código principal

persona1 = Persona('Ana', 'Martinez')
print(persona1) #El metodo  ___str__ se llama automaticamente desde print 

# print(persona1.__str__()) #Esto es opcional 
