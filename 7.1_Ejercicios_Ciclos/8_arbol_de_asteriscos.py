"""""
/*
    Hacer un arbol con '*' del tipo:
    Ejemplo:

    Digite el numero de filas: 5

    *
    **
    ***
    ****
    *****

*/

"""""

cant = int(input("Digite el numero de fila: "))

i = 0 #iteracion en 1 en 1
# j = 0 aqui esta declaracion no funcionara para el codigo 



# while i < cant:
#     j = 0  aqui si funciona 
#     print("") #python por default usa saltod de linea
#     while j <= i:
#         print("*",end='') #end sirve para elimine los saltos de linea
#         j+=1
#     i+=1


for i in range(i,cant + 1):
    j=0   ##Por alguna razon funciona si lo declaro aqui en 0 y no arriba 
    print("")
   
    for j in range(j, i + 1):
        print("*",end="")