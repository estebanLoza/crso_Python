"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada 
una de las correspondientes notas introducidas por el usuario.

"""


materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []


print(len(materias))



for materia in materias:
    nota = input(f"Que nota sacaste en {materia}?: " )
    notas.append(nota) #Aqui indico que en la lista vacia(notas), agrega lo que escribo en nota

for i in range(len(materias)): #Estoy indicando que la cantidad de largo de la lista (5) vas iterar en su posicion 
    print(f"En la materia {materias[i]}, sacaste {notas[i]} ")
        #en materias[i] vas a imprimir             #de la lista notas vas a imprimir lo que hay en su posición
        #lo que hay en su posicion 
        # 0 = matematicas
        # 1 = etc.


