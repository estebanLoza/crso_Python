"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.


Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70



"""


listaFrutas = {
    "Platano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70,
    "Uva": 2.22
}



searchFruta = input("Escribe la fruta: ")
searchFrutaTitle = searchFruta.title()


encontrada = False #bandera para suponer que hasta hora no se ha econtrado  

for buscarFruta in listaFrutas:
    if buscarFruta in searchFrutaTitle:
        kgFruta = float(input("Ingrese la cantidad(kg) de fruta: "))
        
        precioFruta = listaFrutas.get(buscarFruta) #Tomo el precio de la fruta 

        precioFruta *= kgFruta

        print(f"El precio de la fruta {searchFruta} por los {kgFruta} kg, son ${round(precioFruta,2)} Dolares")
        encontrada = True 
        break #ya no necesita buscar 


if not encontrada:
    print("La fruta no esta en a lista")
