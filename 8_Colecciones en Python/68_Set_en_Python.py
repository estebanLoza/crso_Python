#Que son la colección set

#En set no mantiene un orden y no se puede repertir un elemento y no se pueden modificar
#Pero si se puede agregar elementos

#Estructura de tipo set es con {}
planetas = {"Marte", "Jupiter", "Saturno"}

print(planetas)

#Podemos preguntar sobre su largo
print(len(planetas))

#Podemos revisar si un elemento esta presente en un "set"
print("Marte" in planetas)


#Podemos agregar mas elementos
planetas.add("Tierraaa")

print(planetas)


#No soporte elementos Duplicados
planetas.add("Tierraaa")

#Para eliminar un elemento del set
planetas.remove("Marte")
print(planetas)  #*Si el elemento no se encuentra en la lista nos marcara un error, ya que ese elemento no existe para borrarlo
    #otra forma de borrar un elemento, y si no esta el elemento no nos marcara un error
planetas.discard("Jupiter")
print(planetas)

#Para limpiar nuestro set
planetas.clear()
print(planetas)
