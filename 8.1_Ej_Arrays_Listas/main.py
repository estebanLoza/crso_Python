Escritores = {
    "Mario Benedetti":"Escritoro uruguayo nacido en 1920, conocido por su libro 'la tregua'",
    "Gabriel Garcia":"Escritor Colombiano nacido en 1927, conocido por su libro Cien años de Soledad y GANADOR DEL PREMIO NOBEL",
    "Jose Saramago": "Escritor Portugues nacido en 1922, conocido por su libro 'Ensayo sobre la ceguera' y GANADOR DEL PREMIO NOBEL",
    "Charles Bukowski": "Escritor Americano, nacido en 1898",
    "Julio Cortazar": "Escritor Argentino/Fransesm, nacido en Bruselas"
}




def CrearLista():  #Creacion de la lista OPCION 1
    elementos = int(input("Cuantos elementos quiere agregar?: "))
    contador = 1
    listaEscritores = []

    while contador <= elementos:
        elementosLista = input(f"Ingrse el {contador} elemento: ")
        listaEscritores.append(elementosLista)
        contador+=1
    print(listaEscritores)



def BuscarEscritor():#Opcion 2 Buscar Escritor
    nombreEscritor = input("Que escritor quieres buscar?: ")

    if nombreEscritor in Escritores: 
        print(Escritores.get(nombreEscritor))
    else:
        print("El escritor no esta en la lista")
        print("Que quiere hacer?: ")
        print("1)Ver la lista que hay de escritores")
        print("2)Salir")
        op = int(input("Opcion: "))
        
        if op == 1:
            for keys in Escritores.keys():
                print(keys)
        elif op == 2:
            print('Gracias por usar el programa')
        else:
            print("Opcion Invalida")

def LibrosLeidos():
    ListLibrosCompletados = ['La tregua', 'Historias de Cronopio', 'Las Itermitencias de la Muerta', 'Cien años de soledad']

    for lista in ListLibrosCompletados:
        print(lista)

    print('\n')

    print("Que quieres hacer?: ")
    print("1)Agregar un elemnto")
    print("2)Quitar un elemento")
    print("3)Saber la cantidad de libros")
    opcion = int(input("Opcion: "))



    if opcion == 1:
        agregarElemento = input('Escribe el elemento: ')
        ListLibrosCompletados.append(agregarElemento)
        print(ListLibrosCompletados)
        
    elif opcion == 2:
        quitarElemento = input('Escribe el libro que quieres quitar: ')
        ListLibrosCompletados.remove(quitarElemento)
        print(ListLibrosCompletados)

    elif opcion == 3:
        print(len(ListLibrosCompletados))
    else: 
        print("Opcion Invalida, Gracias por usar el programa")
        




print("****BIENVENIDO AL PROGRAMA*****")
print("1)Crear una lista de escritores")
print("2)Buscar Escritores y su información")
print("3)Libros leidos")
print("4)Salir")

op = int(input("Opcion: "))

if op == 1:
    CrearLista()
elif op == 2:
    BuscarEscritor()
elif op == 3:
    LibrosLeidos()
elif op == 4:
    print("Gracias por usar el programa")
else:
    print("Opcion invalida")



