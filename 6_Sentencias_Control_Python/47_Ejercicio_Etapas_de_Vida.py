"""
***EJERCICIO: Etapas de Vida según Edad ***


0 - 10 La ifancia es Increible
10 - 20 Muchos cambios y mucho estudio
20 - 30 Amor y comienza el trabajo

cualquier otro valor: etapa de vida no reconocida

"""

edad = int(input("Proporciona tu edad: "))

if edad >= 0 and edad < 10:
    print("La infancia es increible")
elif edad >= 10 and edad < 20:
    print("Muchos cambios y mucho estudio")
elif edad >=20 and edad <= 30:
    print("Amor y comienza el trabajo")
else:
    print("Etapa de vida no reconocida")