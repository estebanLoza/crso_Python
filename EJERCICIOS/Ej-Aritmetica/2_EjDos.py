"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas
y el coste por hora. Después debe mostrar por pantalla la paga que le
corresponde

"""

horasTrabajadas = float(input("Horas trabajadas: "))

costoPorHora = float(input("Costo por hora: "))

pagoCorrespondiente = horasTrabajadas * costoPorHora

print(f"El pago por las horas trabajadas es de ${pagoCorrespondiente}MXN")
