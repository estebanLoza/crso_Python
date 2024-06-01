#Suma de facotorial
#Ejmplo:
#Digite la cantidad de factorial a sumar: 5
# == 33
#Por que es el factiarl del 1 al 5


facto = int(input("Ingrese hasta que factorial sumar: "))

i = 1 #Punto de arranque e iteracion
suma = 0 #Memoria para guardan la suma
factoMulti = 1 #Me moria para guardar la multiplicaciones y inciar en 1

while i <= facto: 
    factoMulti*=i  #Se multiplica todos las iteraciones y se guarda ahi hasta llegar a la condicion
    suma+=factoMulti #Luego de las multiplicaciones se suman y se guardan ahi
    i+=1
print(f"factorial hasta el numero {facto} es de {factoMulti}")
print(f"La suma total es de {suma}")

