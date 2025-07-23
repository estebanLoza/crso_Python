import requests  # Sirve para ver las imagenes web
from PIL import Image  # abrir imagenes de manera local
from io import BytesIO  # abrir imagenes de web (creo)

#
# listaAutores = [
#     "Mario Benedetti",
#     "Julio Verne",
#     "Isabel Allende",
#     "Julio Cortazar",
#     "Jose Saramago",
#     "Charles Bukowski",
#     "Jorge Luis Borges",
# ]
#
# listaParaAgregarAutores = []  # Esto se usara mas adenlante
#
# listaLibros = [
#     "La Borra De Café",
#     "La Tregua",
#     "El Amor En Tiempos De Cólera",
#     "El Coronel No Tiene Quien Le Escriba",
#     "Las Intermitencias De La Muerte",
#     "El Aleph",
#     "Rayuela",
#     "Historia De Cronopios Y De Faunas",
#     "Mi Nombre Es Emilia del Valle",
#     "El Hombre",
#     "Poesia Completa De Jorge Luis Borges",
#     "Ficciones",
#     "Dialogos",
#     "El Banquete",
#     "La Senda Del Perdedor",
#     "Mujeres",
#     "Escritores De Un Viejo Incidente",
#     "Hijo De Satanas",
#     "Ausencia Del Hereo",
#     "Ensayo Sobre La Ceguera",
#     "El Viaje Del Elefante",
#     "Ensayo Sobre La Lucidez",
#     "Cain",
#     "El Evangelio Segun Jesucristo",
#     "El Hombre Duplicado",
#     "Memorial Del Convento",
#     "Todos Los Nombres",
#     "La Caverna",
#     "El Añio De La Muerte",
#     "El Principito",
# ]


# Creare un diccionario con la info de los libros, para ello se crea un diccionario dentro de otro diccionario.
librosConInformacion = {
    "La Tregua": {
        "Autor": "Mario Benedetti",
        "Sinopsis": "Un diario intimo sobre la rutina, el amor inesperado y la melancolia de la vida cotidiana",
        "Año": 1960,
        "Portada": "https://m.media-amazon.com/images/I/61xcUlIJ24L._AC_UF894,1000_QL80_.jpg",
    },
    "Las Intermitencias De La Muerte": {
        "Autor": "Jose Saramago",
        "Sinopsis": "Una reflexión alegórica donde la muerte deja de actuar en un país, generando caos y dilemas éticos.",
        "Año": 2005,
        "Portada": "https://m.media-amazon.com/images/I/616OAOTn00L._AC_UF894,1000_QL80_.jpg",
    },
    "El Coronel No Tiene Quien Le Escriba": {
        "Autor": "Gabriel García Márquez",
        "Sinopsis": "La historia de un coronel retirado que espera una pensión que nunca llega, en medio de la pobreza.",
        "Año": 1961,
        "Portada": "https://m.media-amazon.com/images/I/81Vx3UjIbZL._SY522_.jpg",
    },
    "El Aleph": {
        "Autor": "Jorge Luis Borges",
        "Sinopsis": "Una colección de cuentos que exploran el infinito, la memoria, los laberintos y la literatura.",
        "Año": 1949,
        "Portada": "https://m.media-amazon.com/images/I/610Upk1dApL._SL1500_.jpg",
    },
    "Ficciones": {
        "Autor": "Jorge Luis Borges",
        "Sinopsis": "Una serie de cuentos filosóficos y metafísicos que desafían la lógica y la realidad.",
        "Año": 1944,
        "Portada": "https://m.media-amazon.com/images/I/31oAt-439BL._SY445_SX342_PQ54_.jpg",
    },
    "Hijo de Satanás": {
        "Autor": "Charles Bukowski",
        "Sinopsis": "Un conjunto de relatos crudos y viscerales que abordan la marginalidad, el alcohol y la crudeza humana.",
        "Año": 1985,
        "Portada": "https://m.media-amazon.com/images/I/41J1ecfPcPL._SY445_SX342_PQ54_.jpg",
    },
    "Caín": {
        "Autor": "José Saramago",
        "Sinopsis": "Una revisión irónica y crítica de episodios bíblicos narrados desde la perspectiva del personaje Caín.",
        "Año": 2009,
        "Portada": "https://m.media-amazon.com/images/I/71OwtzhTctL._SY385_.jpg",

    },
    "Rayuela": {
        "Autor": "Julio Cortázar",
        "Sinopsis": "Una novela experimental que puede leerse de distintas formas, explorando el amor, el arte y la existencia.",
        "Año": 1963,
        "Portada": "https://m.media-amazon.com/images/I/41BYQk8tD-L._SX342_SY445_PQ54_.jpg",
    },
    "El Amor En Tiempos De Cólera": {
        "Autor": "Gabriel García Márquez",
        "Sinopsis": "Una historia de amor duradero y paciente entre dos almas separadas por décadas.",
        "Año": 1985,
        "Portada": "https://m.media-amazon.com/images/I/81YPlYG-b9L._SY385_.jpg",
    },
    "La Borra De Café": {
        "Autor": "Mario Benedetti",
        "Sinopsis": "Una novela nostálgica sobre la infancia, la memoria y el paso del tiempo en Montevideo.",
        "Año": 1992,
        "Portada": "https://m.media-amazon.com/images/I/51nK8omyn9L._SY445_SX342_PQ54_.jpg",
    },
    "Mi Nombre Es Emilia Del Valle": {
        "Autor": "Desconocido",
        "Sinopsis": "Una historia sobre identidad, lucha interior y búsqueda personal.",
        "Año": None,  # Puedes completar el año si lo conoces
        "Portada": "https://m.media-amazon.com/images/I/4115OME2ZgL._SY445_SX342_PQ54_.jpg",
    },
    "Ensayo Sobre La Lucidez": {
        "Autor": "José Saramago",
        "Sinopsis": "Una metáfora política sobre una sociedad donde la mayoría vota en blanco como protesta silenciosa.",
        "Año": 2004,
        "Portada": "https://m.media-amazon.com/images/I/41VrGlEF+TL._SY445_SX342_PQ54_.jpg",
    },
    "El Principito": {
        "Autor": "Antonie de Saint-Exupéry",
        "Sinopsis": "Narra la historia de un niño principe que vive en un pequeño asteroide y llega a la Tierra",
        "Año": 1943,
        "Portada": "https://m.media-amazon.com/images/I/811kjwhnjcS._SY466_.jpg",
    },
}
listaParaAgregarLibros = []


def BusquedaLibrosAutores():
    while True:
        print("\n*******Bienvenido a la biblioteca de libros: ********") 
        print("Que quires hacer?")
        print("\n")
        print("1) Ver la lista de los autores")
        print("2) Buscar el libros")
        print("3) Abrir foto de abrir una imagen")
        print("4) Salir")

        try:  # Aqui esto sirve para que no ingrese un caracter o cualquier otra coas que o sea numero
            op = int(input("Ingrese La opcion que quiere seleccionar: "))
        except (
            ValueError
        ):  # Indicamos que el tipo de valor es erroneo (en este caso es entero)
            print("******Ingresaste un valor no valido")
            print("******Vuelve a escribir")
            continue  # continua con el ciclo

        if op == 1:
            # for verAutores in listaAutores:
            #     print(f"*{verAutores}")
            
            i = 1

            for verAutores in librosConInformacion.values():
               losAutores = verAutores.get('Autor')
                #Agrego un contador para la lista en orden
               print(f"{i}-. {losAutores}")
               i += 1

            print(f"\nEsta el autor que buscas?")

            # hare otro try para que solo la respuesta sea con palabras
            try:
                respAutoresList = input("(Si o No): ")
                autoresLista = respAutoresList.lower()
            except SyntaxError:
                print("**** Ingresaste un caracter invalido ***")
                continue

            if autoresLista == "si":
                print("Gracias por utilizar nuestro busqueda de autores, Buen Dia")
            else:
                print(
                    "Escribe el nombre del autor/es que buscabas para agregarlo en nuestras filas "
                )
                agregaAutro = input("Nombre del Autor@: ")

                print(f"Gracias por sugerirnos a {agregaAutro}. ")

        if op == 2:  # Buscamos los libros
            buscaLibro = input("\nEscribe el nombre del libro por favor: ")
            buscaLibroTitle = buscaLibro.title()

            encontradoElLibro = False

            # como nosotros queremos rastrear si algo paso o no paso
            # durante la ejecucion de un bucle o bloque de codigo
            # en principio se asume que un no se busca

            # buscara si el libro esta

            for elTitulo in librosConInformacion:  # todo la lista en la nueva variable
                if elTitulo == buscaLibroTitle:  # igual a la entrada del titulo
                    if (elTitulo in librosConInformacion):  # si esta en el dicionario y es igual al keys

                        infoDelLibro = librosConInformacion[elTitulo]
                        print("\n\n\n")
                        print(f"\n*****Informacio del libro '{elTitulo}' ****")
                        print(f"\nAño: '{infoDelLibro.get('Año')}' ")
                        print(f"\nSinopsis: '{infoDelLibro.get('Sinopsis')}' ")
                        print(f"\nAutor: '{infoDelLibro.get('Autor')}' ")

                        print(f"\nPortada... {infoDelLibro.get('Portada')} ")
                        print('\n')
                        print("********************************************************")
                        # esto guarda que lo da de valor (value) de Portada (keys) que es el link
                        portada = infoDelLibro.get("Portada")

                        # Esto es el verdadero funcionamiento de que ese pueda abrir la portada
                        response = requests.get(portada, stream=True)
                        imagen = Image.open(BytesIO(response.content))
                        imagen.show()

                    encontradoElLibro = True  # aqui ya buscamos el libro

                    for spaceCode in range(2): #Este for sirve para dar espacios, después de la busqueda.
                        print("\n")

                    break  # salimos del bucle if
            if (not encontradoElLibro):  # aqui ya esta al nivel del for, asi que si al terminar el ciclo "encontrado" sigue siendo false
                print("El libro no se encuentra en la lista.")
        
        #Ejemplo para poder archivos desde la pc
        if op == 3:
            # Uso de ruta para windows abrir img
            imagen_ruta = (
                "C:\\Users\\Esteban\\Pictures\\nikita-palenov-XIMXY5-fK4E-unsplash.jpg"
            )

            imagen_rutaDos = "C:\\Users\\Esteban\\Pictures\\gregBye.jpg"

            imagen = Image.open(imagen_ruta)

            imageDos = Image.open(imagen_rutaDos)

            imagen.show()
            imageDos.show()

        if op == 4:
            print("Gracias por usar el programa")
            break


BusquedaLibrosAutores()
