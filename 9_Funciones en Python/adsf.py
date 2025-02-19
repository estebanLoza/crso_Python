
def sumar(num1, num2):
    suma = num1 + num2

    # print(f"El resultado de la suma es de {suma}")
    return suma

primerNumero = int(input("Ingrese el primer numer: "))

segundoNumero = int(input("Ingrese el segundo numero: "))

resultado = sumar(primerNumero, segundoNumero)

print (f"El valor de la suma es de {resultado} manera 1 dando el resultado guardado en una variable")


print(f"{sumar(primerNumero, segundoNumero)} manera 2 imprimiendo el resultado directamente")