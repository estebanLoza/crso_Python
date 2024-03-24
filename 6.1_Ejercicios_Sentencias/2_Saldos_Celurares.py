"""
Calcular tarifas de saldo en celulares
y poner precios
De 1000 a 1500 premium
De 500 a 999 Intermedia
De 100 a 499 Basica
"""


#SOLO IF ANIDADOS

Tarifa1 = "Premium"
Tarifa2 = "Intermedia"
Tarifa3 = "Basica"


plan = int(input("Ingrese la cantidad de Dinero que quiera Gastar: "))

if plan>=1000 and plan<=1500:
    print(f"Tu presupuesto es para el plan {Tarifa1}")
if plan>=500 and plan<=999:
    print(f"Tu presupuesto es para el plan {Tarifa2}")
if plan>99 and plan<500:
    print(f"Tu presupuesto para el plan es de {Tarifa3}")
else:
    print("Lo siento esa cantidad no entra en los paquetes")

