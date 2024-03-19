"""
Pedirle al usuario que dijite 2 numeros y tenemos que sumarlos, restarlos y multiplicarlos y dividirlos

"""


num1 = float(input("Digite el primer numero: "))

num2 = float(input("Digite el segundo numeor: "))


suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("El resultado de la suma es de ", round(suma,2)) #1 primera manera de escribir un print
print(f"El resultado de la resta es de {round(resta,2)}") #2 segunda manera de escribir un print (segun es el mejor)
print(f"El resultado de la multiplicacion es de {round(multiplicacion)}")
print(f"El resultado de la division es de {round(division)}")





