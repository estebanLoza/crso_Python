""""
Crear una funcion para sumar los valores recbidos de tipo numerico,
utilizando argumentos varibales *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como
argumentos.
"""

def sumar_Valores(*args): # args: (3, 5, 9, 4, 70)
  resultado = 0
  #Iteraciones cada elemento
  for valor in args:
    #Resultaod = resultado + valor
    resultado += valor
  return resultado
  


#Llamdda a la funcion
print(sumar_Valores(3, 5, 9, 70))
