"""


/*
Sumar un numero y restar el siguiente 1-2+3-4+5-6+7



Impares == Positivos
Pares == Negativos


*/

"""
print("***CON CILO FOR***")

numero = int(input("Ingresa hasta que numero se haga la suma/resta: "))

sumaPositivo = 0 #Se guardan los impares
sumaNegativo = 0 #Se guardan los pares
conta =0 #Contador

for conta in range(conta, numero + 1):
    if conta % 2 == 0:
        conta *= (-1) #los numeros pares se convertiran en negativo
        sumaNegativo += conta
    else:
        sumaPositivo+=conta
    
#Suma total de los negativos  y positivos
sumaGeneral = sumaPositivo + sumaNegativo #sumaNegativo por default guarda puro varlo negativo seria asi lo logico + (-sumaengativo) = - regle
                                        #regla de los signos

print(f"La suma/resta hasta el numero {numero} es de {sumaGeneral}")



print("\n")

print("***CON CICLO WHILE****")

num = int(input("Ingresa hasta que numero se haga la suma/resta: "))

sumPos = 0 #Se guardan los impares
sumNeg = 0 #Se guardan los pares
contador =0 #Contador



"""
no se puede hacer lo mismo que for sobre contador*=(-1)
dado que se convierte en la segunda iteracion en 0.5 en python en c si se puede

"""

while contador <= num:
    if contador % 2 ==0:
    
        sumNeg += contador 
    else:
        sumPos += contador
    contador+=1 #el contador esta fuera del if y el se ahi

sumGen = sumPos - sumNeg

print(f"La suma hasta el numero {num} es total de {sumGen}")