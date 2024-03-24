"""
Decirle al alumno algo con base en sus calificaciones
*9-10 -> Excelente, sigue así
8-9 -> Muy bien, puedes mejorar
7-8 -> Eres un estudiante regular
0 - 6.9 -> Puedes Mejorar


*****USO DEL elif******

""" 

calf = float(input("Digita tu calificacion: "))


if calf > 9 and calf <= 10:
    print("Excelente, sigue así")
elif calf >= 8 and calf <= 9:
    print("Muy bien, puedes mejorar")
elif calf >= 7 and calf <= 8:
    print("Eres un estudiante regular")
elif calf >= 0 and calf <= 6.9:
    print("Puedes Mejorar")





