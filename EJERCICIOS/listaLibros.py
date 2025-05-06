listaAutores = [
    "Mario Benedetti",
    "Julio Verne",
    "Isabel Allende",
    "Julio Cortazar",
    "Jose Saramago",
    "Charles Bukowski",
    "Jorge Luis Borges"
]

listaParaAgregarAutores = [] #Esto se usara mas adenlante

listaLibros = [
    "La Borra De Cafe",
    "La Tregua",
    "El Amor En Tiempos De Colera",
    "El Coronel No Tiene Quien Le Escriba"
    "Las Intermitencias De La Muerte",
    "El Aleph",
    "Rayuela",
    "Historia De Cronopios Y De Faunas",
    "Mi Nombre Es Emilia del Valle",
    "El Hombre",
    "Poesia Completa De Jorge Luis Borges",
    "Ficciones",
    "Dialogos",
    "El Banquete",
    "La Senda Del Perdedor",
    "Mujeres",
    "Escritores De Un Viejo Incidente",
    "Hijo De Satanas", 
    "Ausencia Del Hereo",
    "Ensayo Sobre La Ceguera", 
    "El Viaje Del Elefante",
    "Ensayo Sobre La Lucidez",
    "Cain",
    "El Evangelio Segun Jesucristo",
    "El Hombre Duplicado",
    "Memorial Del Convento",
    "Todos Los Nombres",
    "La Caverna",
    "El Añio De La Muerte"
]


#Creare un diccionario con la info de los libros, para ello se crea un diccionario dentro de otro diccionario.
librosConInformacion =  {
    "La Treguea": {
        "Autor": "Mario Benedetti",
        "Sinopsis": "Un diario intimo sobre la rutina, el amor inesperado y la melancolia de la vida cotidiana",
        "Año": 1960
        
    },

    "Las Intermitencias De La Muerte": {
        "Autor": "Jose Saramago",
        "Sinopsis": "Una reflexión alegórica donde la muerte deja de actuar en un país, generando caos y dilemas éticos.",
        "Año": 2005
    },

    "El coronel No Tiene Quien Le Escriba": {
        "autor": "Gabriel García Márquez",
        "sinopsis": "La historia de un coronel retirado que espera una pensión que nunca llega, en medio de la pobreza.",
        "año": 1961
    },

    "El Aleph": {
        "autor": "Jorge Luis Borges",
        "sinopsis": "Una colección de cuentos que exploran el infinito, la memoria, los laberintos y la literatura.",
        "año": 1949
    },

    "Ficciones": {
        "autor": "Jorge Luis Borges",
        "sinopsis": "Una serie de cuentos filosóficos y metafísicos que desafían la lógica y la realidad.",
        "año": 1944
    },

    "Hijo de Satanás": {
        "autor": "Charles Bukowski",
        "sinopsis": "Un conjunto de relatos crudos y viscerales que abordan la marginalidad, el alcohol y la crudeza humana.",
        "año": 1985
    },

    "Caín": {
        "autor": "José Saramago",
        "sinopsis": "Una revisión irónica y crítica de episodios bíblicos narrados desde la perspectiva del personaje Caín.",
        "año": 2009
    },

    "Rayuela": {
        "autor": "Julio Cortázar",
        "sinopsis": "Una novela experimental que puede leerse de distintas formas, explorando el amor, el arte y la existencia.",
        "año": 1963
    },

    "El Amor En Tiepos De Cólera": {
        "autor": "Gabriel García Márquez",
        "sinopsis": "Una historia de amor duradero y paciente entre dos almas separadas por décadas.",
        "año": 1985
    },

    "La Borra De Café": {
        "autor": "Mario Benedetti",
        "sinopsis": "Una novela nostálgica sobre la infancia, la memoria y el paso del tiempo en Montevideo.",
        "año": 1992
    },

    "Mi Nombre Es Emilia Del Valle": {
        "autor": "Desconocido",
        "sinopsis": "Una historia sobre identidad, lucha interior y búsqueda personal.",
        "año": None  # Puedes completar el año si lo conoces
    },

    "Ensayo Sobre La Lucidez": {
        "autor": "José Saramago",
        "sinopsis": "Una metáfora política sobre una sociedad donde la mayoría vota en blanco como protesta silenciosa.",
        "año": 2004
    }
}

listaParaAgregarLibros = [] 



def BusquedaLibrosAutores():
    
    while True:
        print("********Bienvenido a la biblioteca de libros: ********")
        print("\n")
        print("Que quires hacer?")
        print("\n")
        print("1) Ver la lista de los autores")
        print("2) Buscar el libros")
        print("3) Salir")

        try: #Aqui esto sirve para que no ingrese un caracter o cualquier otra coas que o sea numero
            op = int(input("Ingrese La opcion que quiere seleccionar: "))
        except ValueError: #Indicamos que el tipo de valor es erroneo (en este caso es entero)
            print("\n******Ingresaste un valor no valido")
            print("******Vuelve a escribir")
            continue #continua con el ciclo

        if op == 1:
            for verAutores in listaAutores:
                print(f"*{verAutores}")
            print(f"\nEsta el autor que buscas?")
            
            #hare otro try para que solo la respuesta sea con palabras 
            try:
                respAutoresList = input("(Si o No): ")
                autoresLista = respAutoresList.lower()
            except SyntaxError:
                print("**** Ingresaste un caracter invalido ***")
                continue
            
            if autoresLista == "si":
                print("Gracias por utilizar nuestro busqueda de autores, Buen Dia")
            else:
                print("Escribe el nombre del autor/es que buscabas para agregarlo en nuestras filas ")
                agregaAutro = input("Nombre del Autor@: ")

                print(f"Gracias por sugerirnos a {agregaAutro}. ")

        if op == 2: # Buscamos los libros 

            buscaLibro = input("Escribe el nombre del libro por favor: ")
            buscaLibroTitle = buscaLibro.title()

            #buscara si el libro esta 
            if buscaLibroTitle in listaLibros: #indicamos que si esta 
                for buscandolibroInfo in listaLibros: # toda la listaLibros se itera en buscalibroInfo 
                    #print(f"{buscandolibroInfo}")   #verificacion de iteracion 
                    if buscandolibroInfo in librosConInformacion.keys():
                        print(f"{librosConInformacion[buscaLibroTitle]}")
                        
                


        if op == 3:
            print("Gracias por usar el programa")
            break
        else:
            print("Fuera de las opciones de seleccion")



BusquedaLibrosAutores()
