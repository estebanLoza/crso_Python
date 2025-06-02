# Definicion de una clase
# con la palabra reservada class
#


class Persona:
    # metodo (o clase), siempre se inicia la primera letra en mayuscula
    def inicializar_persona(self, nombre, apellido):
        # creacion de los atributos de la clase
        self.nombre = nombre  # --nombre del parametro (nombre, este se debe llamar igual que el que esta en self) y parametro (self.nombre) no importa si parametro se llama self.nom
        self.ap = apellido

    def mostrar_persona(self):
        print(
            f"""Persona: 
            Nombre: {self.nombre}
            Apellido: {self.ap}

        """
        )


# Creacion del primero objetos

# el objeto en este caso sera para ver eel nombre y apellido de la persona 1


# estamos creando un objeto vacio para el espacio de memoria
if __name__ == "__main__":
    # Creacion de un primer objeto
    persona1 = Persona()  # Crea un objeto vacio en memoria
    persona1.inicializar_persona("Layla", "Acosta")

    persona1.mostrar_persona()

    # cracion de un 2 objeto.

    persona2 = (
        Persona()
    )  # creamos un objeto vacio, donde no estamos agregando ninguna informacion
    persona2.inicializar_persona("steban", "arriaga")
    persona2.mostrar_persona()
