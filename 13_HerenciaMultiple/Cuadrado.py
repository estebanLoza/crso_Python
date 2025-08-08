#Este archivo es el 3 y el 2 video sobre la herencia multiple


from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
   
    def __init__(self, lado, color):
       # super().__init__() #Esto no es muy recomandable porque puede dar errores en un futuro
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)


    def calcular_area(self):
        return self.alto * self.ancho


