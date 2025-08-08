from teclado import Teclado
from monitor import Monitor
from raton import Raton


#Creación de la clase para poder usar la app principal
class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton



    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}
        '''






# Codigo principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 27)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1) #pasamos las referencias de los objetos que creamos
    print(computadora1)


    teclado2 = Teclado('Gamer', 'Bluetooth')
    raton2 = Raton('Gamer', 'Bluetooth')
    monitor2 = Monitor('Gamer', 34)
    Computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)
    print(Computadora2)




