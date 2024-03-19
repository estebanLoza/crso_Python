#Area de un trapecio

baseMenor = float(input("Escribe la base menor: "))

baseMayor = float(input("Escribe la base Mayor: "))

altura = float(input("Escribe la altura: "))

area = ((baseMayor + baseMenor)/2) * altura


print(f"El area del trapecio es de {round(area,2)}")