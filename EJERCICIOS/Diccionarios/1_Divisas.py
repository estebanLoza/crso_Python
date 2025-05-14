Divisas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}


print("Bienvenido al programa: ")

divisa = input("Que divisas quiere (Solo tenemos Euro, yen, Dollar): ")


print(Divisas.get(divisa.title()))
