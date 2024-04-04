"""
Dada una nota de un examen mediante un codigo escribir
el literal que le corresponda a la nota.

A - Excelente
B - Notable
C - Aprobado
D y F - Reprobado

"""

nota = input("Escriba su nota: ")

nota = nota.lower() #Para que este comando funcione debes declarar las letras con "" y minusculas

if nota == "a":
    print("Excelente")
elif nota == "b":
    print("Notable")
elif nota == "c":
    print("Aprobado")
elif nota == "d" or nota == "f":
    print("Reprobado")