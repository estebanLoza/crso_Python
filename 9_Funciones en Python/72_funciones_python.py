
"""

ESTO ES UNA ACUTALIZACIÓN DESDE ACODE DE MI TABLET SIN TERMUX

esto es unos ejemplos de funciones con return

"""


print("Argumentos de longitud variable")

def suma(numeros):
  total = 0
  for n in numeros:
    total += n
  return total
    
print(f"{suma([1,3,5,4])}") #manera 1 sin usar el * para pasar todos los arreglos.71_funciones_pyhton.py




print("Segunda forma con * en la funcion para pasar todos los argumentos asi con eso trabajamos con ARGUMENTOS DE LONGITUD VARIBALE")
def sumas(*numeross):
    totall = 0
    for nn in numeross:
      totall += nn
    return totall
print(f'{sumas(1,3,5,4)}')