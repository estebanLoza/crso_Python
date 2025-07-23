class Instrumento: 
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("Estamos tocando musica")

    def romper(self):
        print("Esto lo pagas tu ")
        print(f"Son {self.precio} $$")


class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    pass

bateria  = Bateria(Instrumento)

print(Bateria)
