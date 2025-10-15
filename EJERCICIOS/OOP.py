class Persona:
    def inicializar_persona(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"""
            Nombre:
                Persona: {self.nombre}
                Apellido: {self.apellido}
        """)


if __name__ == "__main__":

    persona1 = Persona()  # para crear el objeto
    persona1.inicializar_persona("Layla", "Acosta")
    persona1.mostrar_persona()

    persona2 = (
        Persona()
    )
    persona2.inicializar_persona("Esteban", "Arriaga")
    persona2.mostrar_persona()
