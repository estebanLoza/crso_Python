##ejemplo de 11_Encapsulamiento Python
#Python cuandoa hace clases no "hace privado " los atributos y métodos de una clases


##**Ejemplo de que una clase que no oculta el Encapsulamiento 
"""
class Clase:
  atributo_Clase = "Hola"
  def __init__(self, atributo_Clase):
    self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
print(f"{mi_clase.atributo_clase}")
print(f"{mi_clase.atributo_instacia}")


"""
#Salida del codigo de arriba
# 'Hola'
# Que tal


#ejemplo verdadero sobre el encapsulamiento que esto hace que quede "privado de alguna manera"
#Ambos atributos son perfectamente accesibles desde el exterior. Sin embargo esto es algo que tal vez no queramos.
#Hay ciertos métodos o atributos que queremos que pertenezcan sólo a la clase o al objeto, y que sólo puedan ser accedidos por los mismos. 
#Para ello podemos usar la doble __ para nombrar a un atributo o método. Esto hará que Python los interprete como “privados”, de manera que 
#no podrán ser accedidos desde el exterior

class Clase:
  atributo_clase = "Hola" #Accesible desde el exterior
  __atributo_clase = "Hola" #No Accesible
  
  # No accesible desde el exterior
  def __mi_metodo(self):
    print("Haz algo")
    self.__variable = 0 
  
  #Accesible desde el exterior
  def metodo_normal(self):
    #El método si es accesible desde el interior
    self.__mi_metodo()
  
mi_clase = Clase()
#mi_clase.__atributo_clase        #Errro! El atributo no es accesible
#print(f"{mi_clase.__atributo_clase}")  #Error! El atributo no es accesible

mi_clase.atributo_clase
print(f"{mi_clase.metodo_normal()}")
  
    
    
    
    
    
    
    
    