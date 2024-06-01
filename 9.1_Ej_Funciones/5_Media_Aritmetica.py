#Hacer un programa que realice la media aritmetica de 2 numero.

def media(num1, num2):
    opMedia = (num1 + num2)/2
    return opMedia

nu1 = float(input("Escriba el primer Numero: "))
nu2 = float(input("Escriba el segundo Numero: "))

print(f"La media es de {media(nu1, nu2)}")