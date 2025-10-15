"""
Un constructor es un metodo especial y se utiliza para crear un objeto, o instanciar una clase
Ademas nos puede servir para crear e inicializar los atributos de un nuevo objeto


*** Ejemplo***

    Imaginemos que tenemos una fabrica de robots.
    Cada vez que nosotros vayamos a crear uno nuevo, necesitamos darle un nombre, color y funciones.
    El constructor es como el manual de inicio que dice:
                "Cuando hagas un nuevo robot, asegúrate de ponerle nombre, edad, etc."

    Ese manual se llama:
                            __init__() en python.



"""

# Creamos una clase llamada persona


class Persona:

    # Este es el constructor, se llama __init__
    # Sirve para darle datos inciales a la persona ( como nombre y apellido )
    def __init__(self, nombre, apellido):
        # Aqui guardamos esos datos en el objeto usando el self
        self.nombre = nombre  # Guardamos el nombre
        self.apellido = apellido  # Guardamos el apellido

    # Este método solo muestra lo que guardamos
    def mostrar_persona(self):
        print(
            f"""Persona: 
         Nombre: {self.nombre}
         Apellido: {self.apellido}
         """
        )


# Aqui empieza el programa
#
if __name__ == "__main__":
    # Creamos la primera persona usando el constructor

    persona1 = Persona("Esteban", "Hernandez")
    persona1.mostrar_persona()  # Mostramos los datos
