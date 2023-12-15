#El usuario proporcionara un valor que este dentro del rango de 0 a 5
#usando comparadores logicos, con mayor a 0 o menor a 5,

valor = int(input("Escribe el valor: "))

#varibles para comprar

valor_minimo = 0
valor_max = 5


                #los parentesis son opcionales
dentroRango = (valor >= valor_minimo)  and (valor <= valor_max)

#solo imprimir el valor booleano
print (dentroRango ,'solo imprime el valor booleano')

if valor:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del rango')