"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros)
calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase Tu índice de masa corporal es <imc>
donde <imc> es el índice de masa corporal calculado redondeado
con dos decimales


"""


pesoUsuario = float(input("Ingrese su peso en kg: "))

estaturaUsuario = float(input("Ingrse su estatura en m: "))

mc = (pesoUsuario/estaturaUsuario)

print(f"Tú indice de masa corporal es de {round(mc, 2)}%")
