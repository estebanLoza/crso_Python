mi_diccionario = {
    "nombre":"Juan",
    "edad":25,
    "ciudad":"EjemploVilla"
}


#Imprime solo los Keys y el value, necesitando afuerza .items
print("Imprimimos ambos valores del diccionario, que es keys y values")
for termino, valor in mi_diccionario.items():
    print(termino, valor)

print("\n")


#imprimimos solo keys del diccionario
print("Imprimimos solo keys del diccionario")
for termino in mi_diccionario.keys():
    print(termino)

print("\n")


#Imprimimos solo los values del diccionario
print("Imprimimos solo los values del diccionario")
for valor in mi_diccionario.values():
    print(valor)