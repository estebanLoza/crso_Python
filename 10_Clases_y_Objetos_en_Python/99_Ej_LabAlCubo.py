#Calcular el Area de un rectangulo con POO y los datos los tiene que dar el usuario
# a = base * alura

class AreaRectangulo:
    def __init__(self, base, altura):
        self.Base = base
        self.Altura = altura

    def area_rectangulo(self):
        return self.Base * self.Altura


base = int(input("Ingrese el base: "))
altura = int(input("Ingrese el altura: "))


Rectangulo1 = AreaRectangulo(base, altura)
print(f"El area del rectangulo es de: {Rectangulo1.area_rectangulo()}")
    
#*Se pueden reautilzar estas variables para otro mas creando otro OBJETO

base = int(input("Ingrese el base: "))
altura = int(input("Ingrese el altura: "))


Rectangulo2 = AreaRectangulo(base, altura)
print(f"El area del rectangulo es de: {Rectangulo2.area_rectangulo()}")
