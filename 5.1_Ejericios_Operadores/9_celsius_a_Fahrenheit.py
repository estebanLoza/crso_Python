#Convertir a Celsius a Fahrenheit



celsius = int(input("Ingresa los Grados Celsius: "))

Fahrenheit = (celsius*(9/5)) + 32

#Fahrenheit = (celsius*(9.0/5.0)) + 32      segun en C los tenia que poner con .0 para que asi pudiera funcionar ya que es algo
                                        #ya que segun es por que no sabe el programa se confunde, bueno no se jaja


print(f"Los Grados Fahrenheit es de {Fahrenheit}")