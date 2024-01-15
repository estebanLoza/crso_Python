#En este ejericio se seguira utilizando sobre los operadores logicos
#Tenemos que preguntar a la persona sobre su edad, si esta persona tiene entre 20 y 30, estara dentro del rango


edad_Persona = int(input('Escribe tu edad: '))


veintes = edad_Persona >= 20 and edad_Persona < 30
print(veintes)

treintas = edad_Persona >= 30 and  edad_Persona < 40
print(treintas)




if veintes or treintas:  #Recordando la logica de or, esta seccion cualquiera de las 2 que sea verdadera el resultado es verdadero
    #print("Dentro del rango (20's) o (30's)")   #se cancela para que no se imprima
    if veintes:
        print("Dentro de los 20´s")
    elif treintas:
        print("Dentro de los 30's ")
    else:
        print("Fuera del rango")
else: 
    print("No esta dentro de los 20's o de los 30's")



print("\n")
print("\n")



print("Este CODIGO ES DE COMO SE DEBE DE ESCRIBIR LAS EXPRESIONES DE OR (CHECAR CODIGO)")
print("\n")

"""ASI ES COMO SE DEBE DE ESCRIBIR SIN SEPARAR TANTO CON ESTAS EXPRESIONES, LO COMUN ES QUE ESTE DENTRO DEL IF"""

edad_Persona = int(input('Escribe tu edad: '))



if (edad_Persona >= 20 and edad_Persona < 30 ) or (edad_Persona >= 30 and edad_Persona < 40):
    print("Dentro del rango 20's o 30's")

else:
    print("No está dentro del rango de los 20's ni 30's")
