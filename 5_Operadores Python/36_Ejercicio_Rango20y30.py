#En este ejericio se seguira utilizando sobre los operadores logicos
#Tenemos que preguntar a la persona sobre su edad, si esta persona tiene entre 20 y 30, estara dentro del rango


edad_Persona = int(input('Escribe tu edad: '))
edad = 0

veintes = edad >= 20 and edad < 30
print(veintes)

treintas = edad >= 30 and  edad < 40
print(treintas)

