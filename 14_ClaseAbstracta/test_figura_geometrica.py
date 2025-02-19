# from Cuadrado import Cuadrado
# from Rectangulo import Rectangulo

from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo


print("Creación Objeto cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(lado=5, color="rojo")
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f"Calculo área cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)


print("Creación Objeto rectángulo".center(50, "-"))
rectangulo1 = Rectangulo(ancho=9, alto=8, color="verde")
rectangulo.ancho = 15
