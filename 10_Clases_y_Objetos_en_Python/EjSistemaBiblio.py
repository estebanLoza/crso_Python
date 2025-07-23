"""
        TEMA 210 AL FINAL 


    Ejercicio de Sistema de Bibliotecas

    Se debe aplicar la programación orientada a objetos para resolver
    este problema

    Un libro tiene los atributos de título, autor y género. Debe aplicar el concepto
    de encapsulamiento

    por otro lado una biblioteca contiene un nombre, así como una lista de libros.

    Además tiene los siguientes métodos para administrar los libros.

    * Agregar libros 
    * Buscar libros para autor
    * Buscar libros por género
    * Mostrar todos los libros
    * Mostrar un libro

    Además debe aplicar encapsulamiento


"""


class Libro:

    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    # solo lectura
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero
