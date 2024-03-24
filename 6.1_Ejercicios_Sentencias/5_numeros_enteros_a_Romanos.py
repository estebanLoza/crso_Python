#Convierte Numeros a numeros romanos.
#Solo hasta millar(miles)

numero = int(input("Ingresa el numero: "))

unidad = numero%10 ; 
numero = numero//10
print(f"Mudulo unidad {unidad}") # doble // es para que se mantenga un numero Entero
print(numero)

decena = numero%10 ; 
numero = numero//10
print(f"Mudulo unidad {decena}")
print(numero)

centena = numero%10 ; 
numero = numero//10
print(f"Mudulo unidad {centena}")
print(numero)

millar = numero%10 ; 
numero = numero//10

print(numero)









"""
La importancia de este codigo sobre como se acomoda primero las millas es importante para que asi pueda lerse
ya que recordemos que el codigo se lee lineal de arriba hacia abajo.

"""


