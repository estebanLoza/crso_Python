# Creamos la clase


class Persona:
    # Creamos constructor
    def __init__(self, nombre, apellido):
        # cramos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    # Creamos el metodo: Accion que puede realizar el objeto
    def mostrar_persona(self):
        print(f""" Persona: 
            Nombre: {self.nombre}
            Apellido: {self.apellido}
        """)

    # def mostrar_personaDOs():
    #     print("hola mundo")


# Creacion de objetos

if __name__ == "__main__":
    # Creacion de un primer persona
    persona1 = Persona("Estaban", "Hernandez")
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona("Ian", "Lorenzo")

    persona2.mostrar_persona()
