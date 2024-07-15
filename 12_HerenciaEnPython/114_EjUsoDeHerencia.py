"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""



class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return f"Color {self.color}, Ruedas:  {self.ruedas}"



 #Clases hijas
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad): #Se agrega "velocidad"
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
#super() llamamos el contenido de la clase padre y __str__ es para llamar el return de la clase padre
        return f" {super().__str__()}, Velocidad (Km/hr): {str(self.velocidad)}" #el valor de la velocidad la covertimos a string




class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Tipo de bicicleta:  + {self.tipo}"
 



#Clase Padre
vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)



#Hijo Coche
coche = Coche("Azul", 4, 150) #Los primeros valores son de la clase padre

print(coche)


#Hija Bicicleta
bici = Bicicleta("Azul",4, "montaña")

print(bici)