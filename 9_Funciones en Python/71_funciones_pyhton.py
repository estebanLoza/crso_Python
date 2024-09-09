#Creacion de funciones en python
#Esta una función sin retorno


def mi_funcion():
    i = 1
    while i <= 10:
        print(f'Hola desde la funcion{i}')
        i+=1

mi_funcion() #Una manera de llamar una fucion
print("\n\n\n")
llamarFuncion = mi_funcion()



print("Segundo ejemplo de una funcion")

def f(x): #creamos una funcion que llama 'f' 
  return 2*x   #esta funcion regresara un valor que el valor que escribamos en el parametro de x se multiplicara

y = f(3)  #la variable guarda la funcion 'f ' y le damos un valor al parametro de esa función
print(y)



print("\n\n\n")
#funciones pasando argumentos de entrada

print("Pasando argumentos a funciones")


def diHola(nombre):
  print(f'Hola {nombre}')

diHola('Esteban')


print("\n\n\n\n")

print("funciones pasando Argumentos por posicion")

def resta(a,b):
  return a-b
print(f"{resta(5,3)}") #en este caso se tuvo de poner asi la funcion para que pudiera ver el resultado matematico



