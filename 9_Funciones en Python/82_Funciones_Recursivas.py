#Ejemplo de factorial

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    

resultado = factorial(3)

print(f"El factorial es de {resultado}")
