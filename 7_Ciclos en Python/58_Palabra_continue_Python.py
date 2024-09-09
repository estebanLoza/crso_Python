"""
El uso del continue tiene  casi la misma función que el ´break´ que tambien nos permite modificar
el comportamiento de los ciclos while y for




a diferencia de break que se interrumpe y se termina el  ´continue´ se salta todo el codigo
restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.


En pocas palabras pasa la siguiente iteración saltando el código pendiente.


"""





print("Ejemplo de continue con for y una cadena")
print("Cadena 'Python' y si aparece la letra 'P' (asi  con la letra P) ")

cadena =  'Python'

for letra in cadena:
	if letra == 'P':
		continue
	print(letra)

# Salida:
# y
# t
# h
# o
# n




print("Segundo ejemplo con  'while'")


x = 5

while x > 0:
	x -= 1
	if x == 3:
		continue
	print(x)




