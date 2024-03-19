"""
Dadas las horas trabajadas de una persona y el valor por hora.
Calcular su salario e imprimirlo

"""


horas = int(input("Ingrese las horas trabajadas: "))

pagoHoras = int(input("La cantidad que se paga por horas: "))


total = horas * pagoHoras


print(f"La cantidad que se le paga por las horas trabajadas es de {total}")
