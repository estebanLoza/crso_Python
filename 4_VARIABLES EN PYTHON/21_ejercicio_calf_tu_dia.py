#Este ejercicio tenemos que calificar nuestro dia del 1 al 10

nombre = input("Como te llamas?: ")

print("Bienvenido ", nombre, "Por favor reliza la siguiente calificación")

califDiaLunes = int(input ("Escribe del 1 al 10 el Lunes: "))

califDiaMartes = int(input("Escribe del 1 al 10 el Martes: "))

califDiaMiercoles = int (input ("Escribe del 1 al 10 el Miercoles: "))

promedio = califDiaLunes + califDiaMartes + califDiaMiercoles/3


print ("Tu promedio de los 3 dias que escibiste fue de ", round(promedio,2) , "Muchas gracias ", nombre)
