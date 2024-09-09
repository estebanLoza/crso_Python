"""
Esta sentecia sobre el uso de 'break' nos permite alterar el comporamiento sobre el uso de los bucles 'while' y 'for'

Por ejemplo si queremos buscar una palabra con alguanos de estos
bucles, podemos usar esto y terminar antes, asi evitamos usar recursos de mas e inecesarios.

"""


print("Break con For")

"""
Veamos como podemos usar el break con bucles for. El range(5) generaría 5 iteraciones, donde la i valdría de 0 a 4. Sin embargo, en la primera iteración, terminamos el bucle prematuramente.

El break hace que nada más empezar el bucle, se rompa y se salga sin haber hecho nada.
"""


for i in range(5): #recordemos que el rango es -1 cuando no indicamos, osea este rango es de 0 a 4 
  print(i)
  break
  #No llega
  
  
"""
Otro ejemplo con for mas util
Un ejemplo un poco más útil, sería el de buscar una letra en una palabra. Se itera toda la palabra y en el momento en el que se encuentra la letra que buscábamos, se rompe el bucle y se sale.

Esto es algo muy útil porque si ya encontramos lo que estábamos buscando, no tendría mucho sentido seguir iterando la lista, ya que desperdiciaríamos recursos.

""" 
print("\n\n Otro ejemplo con for mas util")

cadena = 'Python'
for letra in cadena:
  if letra == 'h':
    print(" Se encontro la letra 'h'")
    break
  print(letra)
  
  # Salida:
# P
# y
# t
# Se encontró la h
 #**Esta seria la salida como vemos no se ve lo demas letras com o y n, ya que en la posicion h se rompio.
#**indicamos en el for que imprimer una cadena que se enconro la letra h



