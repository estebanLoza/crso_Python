class Orden:
        
    contador_ordenes = 0

    def __init__(self, computadores):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        
        #Recibimos la lista de objetos de tipo computadora
        self.computadoras = computadores


    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)


    def __str__(self):
        #vamos a iterar todas las computadoras y lo vamos a guardar en la lista de cadenas
        computadoras_str = '' #se crea la cadena vacia


        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()

        return f'''Ordern {self.id_orden}
        Computadoras: {computadoras_str}'''
