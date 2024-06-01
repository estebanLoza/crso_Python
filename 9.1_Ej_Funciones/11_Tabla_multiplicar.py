""""
Hacer un programa que muestre una tabla de multiplicar hasta el 20 de un numero cualquiera por pantalla, el numero se
pide en la funcion principal. Usar procedimiento.
"""""


#!ESTE ES MI VERSION MALA
""""
def tabla_de_Multiplicar(numero):
    contador = 1
    for contador in range(20, 1):
        result = numero *contador
        print(f"{numero} x {contador} = {result}")
    
numero = int(input("INgrse el numero: "))"
tabla_de_Multiplicar(numero)
"""""""""
def tabla_de_Multiplicar(numero):
    for contador in range(1, 21):  # Cambié el rango para que vaya de 1 a 20
                                    #Por lo tanto, si quieres que el bucle vaya desde 1 hasta 20 (inclusive), necesitas especificar el rango como range(1, 21).

                                    #Por ejemplo, si especificas range(1, 21), 
                                    #el bucle recorrerá los números del 1 al 20, incluyendo el 1 pero excluyendo el 21.
                                    
                                    
                                    
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")

numero = int(input("Ingrese el número: "))
tabla_de_Multiplicar(numero)
