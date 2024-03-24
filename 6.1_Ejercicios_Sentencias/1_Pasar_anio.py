#Ver si el alumno va a pasar el año o no
#Un alumno solo tiene derecho a reprobar 3 materias para poder pasar de año
#Si reprueba 4 materias no puede pasar y recursa


materiasRepro = int(input("Ingresa cuantas Materias Reprobaste?: "))


if materiasRepro < 4:
    print(f"Felicidades Apruebas el año con las {materiasRepro}")
else:
    print(f"Repruebas el año con 4 o más materias y tu tienes {materiasRepro}")
    