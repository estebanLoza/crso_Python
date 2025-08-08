from dispositivo_entrada import DispositivoEntrada
#Estos es unos de los dispositivos de entrada 
#contexto estatico y contexto dinamico (temas)


class Raton(DispositivoEntrada):
    #Variable Abstacta (como una variable global pero en poo python)
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada #forma uno de agregar los atributos padre 
        super().__init__(marca, tipo_entrada) #llamando los constructores de la clase Padre

    def __str__(self):
        return (f'Id: {self.id_raton}, Marca: {self.marca},'
                f'Tipo Entrada: {self.tipo_entrada}')




#Codigo principal
if __name__ == '__main__':

    raton1 = Raton('Hp', 'USB')
    print(raton1)
    raton2 = Raton("Acer", "Bluetooth")
    print(raton2)


