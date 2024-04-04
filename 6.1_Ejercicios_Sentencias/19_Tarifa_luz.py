"""
/*Visualizar la tarifa de la luz segun el gasto de corriente
electrica

Par un gasto menor de 1,000kwxh la tarifa es de 1.2, 
entre 1,000 y 1.850Kwxh es 1.0
y mayor de 1,850Kwxh 0.9

*/

"""
tarifa1 = 1.2
tarifa2 = 1.0
tarifa3 = 0.9


gastoCorriente = float(input("Ingrese su tarifa de luz: "))

if gastoCorriente < 1000:
    gastoCorriente = tarifa1
elif gastoCorriente >= 1000 and gastoCorriente <= 1850:
    gastoCorriente = tarifa2
elif gastoCorriente > 1850:
    gastoCorriente = tarifa3

print(f"Su tarifa de luz es de {gastoCorriente}")
    
