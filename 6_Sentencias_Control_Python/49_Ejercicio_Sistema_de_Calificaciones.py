"""
***EJERCICIO: Sistema de Calificaciones***

Instrucciones

El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionar un valor entre 0 y 10.

Si está entre 9 y 10: Imprimir una A
Si está entre 8 y menor a 9 : Imprimir una B
Si está entre 7 y menor a 8: Imprimir una C
Si está entre 6 y menor a 7: Imprimir una D
Si está entre 5 y menor a 6: Imprimir una F
Calquier otro valor debe imprimir: Valor incorrecto

Por ejemplo:
Porporciona un valor entre 0 y  10:



"""

calf = float(input("Igresa tu calificacion: "))

if 9 <= calf <= 10:  # Manera simplificada y diciendo que es mayor y igual
    print("A")
elif calf >= 8 and calf < 9:
    print("B")
elif calf >= 7 and calf < 8:
    print("C")
elif calf >= 6 and calf < 7:
    print("D")
elif calf >= 0 and calf < 6:
    print("F")
else:
    print("Valor incorrecto")
