#Convierte Numeros a numeros romanos.
#Solo hasta millar(miles)

numero = int(input("Ingresa el numero: "))

unidad = numero%10 ; numero = numero // 10 #Se pone doble / para que el sea entero la division 
decena = numero%10 ; numero = numero // 10
centena = numero%10 ; numero = numero // 10
millar = numero%10 ; numero = numero // 10



if millar == 1:
    print(f"M", end='')  #Parametro que ayuda que todo sea en una sola linea
elif millar == 2:
    print(f"MM", end='')
elif millar == 3:
    print(f"MMM", end='')
elif millar == 4:
    print(f"/IV", end='')


if centena == 1:
    print(f"C", end='')
elif centena == 2:
    print(f"CC", end='')
elif centena == 3:
    print(f"CCC", end='')
elif centena == 4:
    print(f"CD", end='')
elif centena == 5:
    print("D", end='')
elif centena == 6:
    print("DC", end='')
elif centena == 7:
    print("DCC", end='')
elif centena == 8:
    print("DCCC", end='')
elif centena == 9:
    print("CM", end='')

if decena == 1:
    print(f"X", end='')
elif decena == 2:
    print(f"XX", end='')
elif decena == 3:
    print(f"XXX", end='')
elif decena == 4:
    print(f"XL", end='')
elif decena == 5:
    print(f"L", end='')
elif decena == 6:
    print(f"LX", end='')
elif decena == 7:
    print(f"LXX", end='')
elif decena == 8:
    print(f"LXXX", end='')
elif decena == 9:
    print(f"XC", end='')

if unidad == 1:
    print(f"I", end='')
elif unidad == 2:
    print(f"II", end='')
elif unidad == 3:
    print(f"III", end='')
elif unidad == 4:
    print(f"IV", end='')
elif unidad == 5:
    print(f"V", end='')
elif unidad == 6:
    print(f"VI", end='')
elif unidad == 7:
    print(f"VII", end='')
elif unidad == 8:
    print(f"VIII", end='')
elif unidad == 9:
    print(f"IX", end='')






"""
La importancia de este codigo sobre como se acomoda primero las millas es importante para que asi pueda lerse
ya que recordemos que el codigo se lee lineal de arriba hacia abajo.

"""


