"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y
un cliente desea saber cuanto debera pagar finalmente por su compra

"""

compra = float(input("Ingrese el total de la Compra: "))

descuento = 0.15

pago_con_Descuento = compra * descuento

descuentoTotal = compra - pago_con_Descuento

print(f"El precio a pagar con el descuento incluido es de {round(descuentoTotal,2)} MXN y el descuento fue de {pago_con_Descuento} MXN" )
