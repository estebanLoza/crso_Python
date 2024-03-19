"""
Tranformar años a meses
Meses a semanas
Semanas a dias
y dias a horas


1 año = 12 meses
1 mes = 4 semanas
1 semana = 7 dias
1 dia = 24 horas

Pedirle al usuario la cantidad de años con las que hara la conversion


"""

nombre = input("Ingrese su nombre: ")

anios = int(input(f"{nombre} ingrese la cantidad de anios que tienes para hacer la conversion: "))


meses = anios * 12
semanas = meses * 4
dias = semanas * 7
horas = dias * 24


print(f"Tu edad en meses es de {meses}")
print(f"Tu edad en semanas es de {semanas}")
print(f"Tu edad en dias es de {dias}")
print(f"Tu edad en horas es de {horas}")


 





