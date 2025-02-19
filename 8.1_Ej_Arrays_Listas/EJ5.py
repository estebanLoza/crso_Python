"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

"""


materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

notas = []


for mat in materias:
    nota = int(input(f"Que nota sacaste en {mat}: "))
    #agrego los valores de nota a la lista vacia "notas"    
    if nota >= 6:
        notas.append(mat)

#Vulevo a usar la variable mat, y hora de toda lista que se guardo en notas.
for mat in notas:
    materias.remove(mat)
    #Aquí indico que de la lista materias vas a eliminar lo que hay en la variable mat (lo que iteramos desde la lista notas.)

print(f"Tienes que repertir {str(materias)}")













# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# passed = []
# for subject in subjects:
#     score = float(input("¿Qué nota has sacado en " + subject + "?"))
#     if score >= 5:
#         passed.append(subject)
# for subject in passed:
#     subjects.remove(subject)
# print("Tienes que repetir " + str(subjects))

