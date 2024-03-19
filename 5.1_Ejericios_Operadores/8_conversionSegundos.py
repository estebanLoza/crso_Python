"""
Calcular la cantidad total de segundos que estan incluidos en el numero de horas,
minutos y segundos ingresados por el usuario.

"""

horas = int(input("Ingrsa la cantidad de horas: "))

minutos = int(input("Ingresa la cantidad de minutos: "))

segundo = int(input("Ingresa la cantidad de segundos: "))


horas *= 3600

minutos *= 60

totalSegundos = horas + minutos + segundo


print(f"La cantidad total de segundos es de {totalSegundos}")




