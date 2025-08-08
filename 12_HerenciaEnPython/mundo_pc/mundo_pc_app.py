from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado



print('**** Mundo Pc ****')


#Empezamos a crear objetos para crear computadoras
#Si observamos esto se copio tal cual como el codigo del archivo
#computadora.py y usamos las bases para crear las computgadoras





# Computadora 1 

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer', 'Bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)


#Crear la lista de computadoras (orden)
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
#print(orden1) #ejemplo

teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', 27)
computadora3 = Computadora('Dell',monitor3,teclado3,raton3)
orden1.agregar_computadora(computadora3) #Se agrega a la orden 1 a pesar que no estaba en la lista de arriba
print(orden1)


#Creamos una segunda orden de computadoras

teclado4 = Teclado('Redragon', 'Bluetoot, USB, 2.4G')
raton4 = Raton('Logitech', 'USB')
monitor4 = Monitor('Quaroni', 29)
computadora4 = Computadora('Chuwi', monitor4, teclado4, raton4)



# teclado5 = Teclado('Redragon', 'Bluetoot, USB, 2.4G')
# raton5 = Raton('Logitech', 'USB')
# monitor5 = Monitor('Quaroni', 29)
# computadora5 = Computadora('Chuwi', monitor4, teclado4, raton4)
#
#
# computadoras2 = [computadora4, computadora5]

computadoras2 = [computadora4]

orden2 = Orden(computadoras2)
print(orden2)

