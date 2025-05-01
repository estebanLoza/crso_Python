listaAutores = [
    "Mario Benedetti",
    "Julio Verne",
    "Isabel Allende",
    "Julio Cortazar",
    "Jose Saramago",
    "Charles Bukowski",
    "Jorge Luis Borges"
]

listaLibros = [
    "La borra de Cafe",
    "La tregua",
    "El amor en tiempos de Colera",
    "El coronel no tiene quien le escriba",
    "Las intermitencias de la muerte",
    "El Aleph",
    "Rayuela",
    "Historia de cronopios y de faunas"
]


def BusquedaLibrosAutores():
    
    while True:
        print("Bienvenido a la biblioteca de libros: ")
        print("\n\n")
        print("Que quires hacer?")
        print("\n")
        print("1) Ver la lista de los autores")
        print("2) Ver la lista de los libros disponibles")
        print("3) Salir")
        op = int(input("Escribe el numero de la selección: "))

        if op == 1:
            for listaAut in listaAutores:
                print(f"{listaAut}")

            respuestaAut = input("El libro autores que buscas esta ? (si o no): ")

            
            if respuestaAut in "si":
                print("Genial,")
            
            else:
                respuestaAutAgregar = input("Lamentamos mucho, quires agregarlo?(si o no): ")

                if respuestaAutAgregar in "si":

                    AgregandoAutor = input ("Escribe el nombre")

                    listaAutores.append(AgregandoAutor)

                    for listaAgregadoAutor in listaAutores:
                        print(f"{listaAgregadoAutor}")

                    print(f"Se agrego a la lista a ' {AgregandoAutor} ', gracias por la aportación")
                    print("\n")
                else:
                    print("Gracias y lamentamos mucho")
        elif op == 2:    
            print("Gracias Adios")
            break;      

BusquedaLibrosAutores()
