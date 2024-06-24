#Se hara un programa que se calcule el volumen de un cubo
#la formula es Volumen = ancho * profundidad * alto

class Cubo:
    def __init__(self, ancho, profundidad, alto):
        self.ancho = ancho
        self.profundidad = profundidad
        self.alto = alto

    def volumen_cubo(self):
        return self.ancho * self.profundidad * self.alto


anchoV = int(input("Ingrese el valor de ancho: "))

profV = int(input("Ingrese el valor de profundidad: "))

alto = int(input("Ingrese el valor de alto: "))

volumenCubo = Cubo(anchoV,profV, alto)

print(f"El volumen es de: {volumenCubo.volumen_cubo()} m3")