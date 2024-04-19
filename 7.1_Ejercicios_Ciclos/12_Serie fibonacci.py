#Serie fibonacci

#0 1 1 2 3 4 5 8 13
#Esta serie va sumando el anterior
#Pedirle al usario hasta que posicion quiere ver la serie

posicion = int(input("Digite hasta que posicion quiere ver: "))

 
x = 0  #Por que inicia 0 la serie
y = 1
z = 1
i = 1 #Para for

print("0, 1",end="")

while i < posicion: #Con for no 
    z = x + y
    x = y
    y = z
    print(f", {z}",end="")
    i+=1

   



