
""" 
    ****SE VEN ALGUNAS MEJORES DE LA SINTAXIS DE LOS OPERADORES LOGICOS.

                                    "AND"
"""

#En este ejericio se seguira utilizando sobre los operadores logicos
#Tenemos que preguntar a la persona sobre su edad, si esta persona tiene entre 20 y 30, estara dentro del rango


"""ASI ES COMO SE DEBE DE ESCRIBIR SIN SEPARAR TANTO CON ESTAS EXPRESIONES, LO COMUN ES QUE ESTE DENTRO DEL IF
                    ***************************************************************
                    *        SINTAXIS SIMPLIFICADA DE OPERADOR AND                *
                    ***************************************************************


"""

edad_Persona = int(input('Escribe tu edad: '))


#LO QUE SE MEJORA LA SINTAXIS ES ESTO (COMPARA CON EL ARCHIVO ANTERIOR)
if (  20 <= edad_Persona < 30 ) or (  30 <= edad_Persona < 40):
    print("Dentro del rango 20's o 30's")

else:
    print("No está dentro del rango de los 20's ni 30's")
