from biblioteca import Biblioteca
from EjSistemaBiblio import Libro


# Este es la app de la prueba del sistemas de biblioteca, de las apps 210_EjSistemaBiblio y biblioteca para poder ejecutarlo

bibliotecaNacional = Biblioteca('Biblioteca Nacional')

print(f"**** Bienvenidos a la {bibliotecaNacional.nombre} ***")

# Definicion de libros
libro1 = Libro("Cien años de Soledad", "Gabriel Garcia Marquez", "Ficcion")
libro2 = Libro("La tregua", "Mario Benedetti", "Romance")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Comedia")


# Agregar los libros a la biblioteca

bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)


# Buscar libros por autor

autor = "Gabriel Garcia Marquez"
print(f"\nLibro de {autor}")


# Buscar libros por genero

genero = 'Ficcion'

print(f"\nLibros de {genero}")

bibliotecaNacional.buscar_libros_por_genero(genero)


# Mostrar todos los libros que hemos creado

print("Mostar todos los libros de la blibioteca nacional")
bibliotecaNacional.mostrar_todos_los_libros()
