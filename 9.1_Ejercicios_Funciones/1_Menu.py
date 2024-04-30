#FUNCION SIN VALOR DE RETORNO

def suma():
  num1 = int(input("Ingrese el primer numero: "))
  num2 = int(input("Ingrese el segundo numero: "))
  
  suma = num1 + num2
  print(f"El resultado de la OPERACION SUMA es de {suma}")

def resta():
  num1 = int(input("Ingresa el primer numero: "))
  num2 = int(input("Ingresa el segundo numero: "))
  
  resta = num1 - num2
  
  print(f"El resultado de la RESTA es de {resta}")

def multiplicacion():
  num1 = int(input("Ingrese el primer numero: "))
  num2 = int(input("Ingrese el segundo numero: "))
  
  multiplicacion = num1 * num2
  
  print(f"El resultado de la MULTIPLICACION es de {multiplicacion}")

def division():
  num1 = int(input("Ingrese el primer numero: "))
  num2 = int(input("Ingrese el segundo numero: "))
  
  division = num1 // num2
  
  print(f"El resultado de la operacion DIVISION es de {division}")

while True:
  print("\n****Bienvenido al PROGRAMA MENU EN PYHTON****")
  print("Eliga una de las siguientes opciones en operaciones: ")
  print("1)Suma")
  print("2)Multiplicacion")
  print("3)Division")
  print("4)Resta")
  print("5)SALIR")
  op = int(input("Opcion: "))
  
  if op == 1:
    suma()
  elif op == 2:
    multiplicacion()
  elif op == 3:
    division()
  elif op == 4:
    resta()
  elif op == 5:
    print("Gracias por usar el programa con FUNCIONES EN PYTHON")
    break
  else:
    print("Opción inválida. Por favor, elija una opción válida.")
  