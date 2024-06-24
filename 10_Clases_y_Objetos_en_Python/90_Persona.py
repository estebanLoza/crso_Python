#TENEMOS QUE RECORDAR QUE EL NOMBRE POO SE PONE CON EL NOMBRE DEL ARCHIVO COMO BUENA PRACTIA, POR AHORA
#NO ES ASÍ DEBIDO POR EL CURSO

class Persona:  #Manera bien, pero no se usa este metodo para hacerlo   
    def __init__(self):
        self.nombre = "Juan"
        self.apellido = "Hernandez"
        self.edad = 24  

#* SE CREA ESTA VARIABLE PARA GUARDARLO Y LO IMPRIMA

persona1 = Persona()
print(f"{persona1.nombre}")
print(f"{persona1.edad}")
print(f"{persona1.apellido}")