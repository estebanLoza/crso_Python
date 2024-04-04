""""
Una distribuidora de motocicletas tiene una promocion de
fin de año que
consiste en los siguiente.Las motos 
Honda tiene un descuento del 5%
las marcas Yamaha del 8% y 
las Suzuki del 10%, 
las otras marcas 2%

"""

nombre = input("Ingrese el nombre de la marca: ")

precio = float(input("Ingrese el precio de la moto: "))

nombre = nombre.lower() 

total = None

if nombre == "honda":
    descuento = precio * 0.05
    total = precio - descuento
    print(f"El total de la mota Honda es de {total}")
elif nombre == "yamaha":
    descuento = precio * 0.08
    total = precio - descuento
    print(f"El precio de la moto Yamaha es de {total}")
elif nombre == "suzuki":
    descuento = precio * 0.1
    total = precio - descuento
    print(f"El precio de la Suzuki es de {total}")
else:
    descuento = precio * 0.02
    total = precio - descuento
    print(f"El precio de marca {nombre} es de {total}")
     






