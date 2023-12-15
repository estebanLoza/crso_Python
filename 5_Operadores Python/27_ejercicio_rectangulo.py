"""
En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo, para ello deberemos
crear los siguientes varibales: 

alto (int)
ancho (int)

Debe de quedar de la siguiente manera respetando los espacios, mayúsculas, minusculas, etc.

Proporciona el alto del rectangulo: 
Proporciona el ancho del rectangulo: 
Area: 
Perimetro


Formula del Area: Alto * ancho

Formula del perimetro: (alto + ancho)*2
"""

alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))

area = alto * ancho
perimetro = (alto + ancho)*2


"""         MANERA TRADICIONAL SOBRE COMO IMPRIMIR

print("Area: ", area)
print("Perimetro: ", perimetro)

"""

"""SEGUNDA MANERA SOBRE COMO ES MAS EFICIENTE EL CODIGO"""

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")





