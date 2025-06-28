lista = []


p = int(input("Ingresa la cantidad de datos que quieres guardar: "))

for i in range(p):
    datosGuardar = input(f"Ingrea el {i + 1} dato: ")
    lista.append(datosGuardar)

print("\n\n")

for numeroPrint in range(len(lista)):
    print(f" '{lista[numeroPrint]}' es el {numeroPrint + 1} de la lista")
