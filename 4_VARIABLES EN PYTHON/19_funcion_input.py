#Funcion input para procesar la entrada del usuario

#CON NUMEROS

#primero se asigna una variable, donde se le asignara un valor que nosotros escribimos

num1 = input("Escribe un numero: ")

print (num1, " Es el valor que escribiste")




#CON TEXTO

valor = input ("Escribe un mensaje; ")

print("Este el es mensaje ", valor)  #LA FUNCIÓN INPUT, regresa un tipo string (str)



#Input recibe cualquier tipo de parametro, pero SIEMPRE LO REGRESARA UN STRING  (STR), asi que para ser sumas, resta, etc, tenemos que declarar
#que usaremos 


num1 = int(input("Escribe el numero 1: "))
num2 = int(input("Escribe el numero 2: "))

resultado = num1 + num2

print ("El resultado es de ", resultado)
