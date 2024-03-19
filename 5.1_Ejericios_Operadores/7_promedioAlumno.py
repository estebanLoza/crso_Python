"""
Un alumno desae saber cual sera su calificacion final en la
materia de Algoritmos

Dicha calificacion se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificacion del examen final
15% de la calificacion de un trabajo final
"""


p1 = float(input("Ingresa la calificacion del primer Parcial: "))

p2 = float(input("Ingresa la calificacion del Segundo Parcial: ")) 

p3 = float(input("Ingresa la calificaicon del Tercer Parcial: "))


examenFinal = float(input("Ingrsa la calificacion del Examen Final: "))

trabajoFinal = float(input("Ingrsa la calificacion del Trabajo Final: "))


promedioParcial = (p1 + p2 + p3) / 3

promedioParcial *= 0.55

print(f"Calificacion del los Parciales {round(promedioParcial,2)} %")


examenFinal *= 0.30

trabajoFinal *= 0.15

promedioFinal = promedioParcial + examenFinal + trabajoFinal

print(f"Promedio final {round(promedioFinal,2)}")





