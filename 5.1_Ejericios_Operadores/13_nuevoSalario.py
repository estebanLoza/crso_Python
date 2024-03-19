""""
Calcular el nuevo salario de un obrero
si obtuvo un incremento del 25% sobre su salario anterior

"""


salario = float(input("Ingrese su salario: "))

porcentaje = 0.25

aumento = salario * porcentaje

incrementoSalario = salario + aumento

print(f"Su aumento con el 25% es de ${round(aumento,2)} MXN y el total de su nuevo Salario es de ${round(incrementoSalario,2)} MXN")