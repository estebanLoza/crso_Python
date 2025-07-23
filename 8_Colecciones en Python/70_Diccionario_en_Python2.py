mi_diccionario = {
    "nombre":"Juan",
    "edad":25,
    "ciudad":"EjemploVilla"

}


#Imprime solo los Keys y el value, necesitando afuerza .items
print("Imprimimos ambos valores del diccionario, que es keys y values")
for clave, valor in mi_diccionario.items():
    print(clave, valor)

print("\n")


#imprimimos solo keys del diccionario
print("Imprimimos solo keys del diccionario")
for clave in mi_diccionario.keys():
    print(clave)

print("\n")


#Imprimimos solo los values del diccionario
print("Imprimimos solo los values del diccionario")
for valor in mi_diccionario.values():
    print(valor)


#Ejemplos con un diccionario anidado

datos = {
    'estudiante1': {
        'nombre': 'Juan',
        'edad': 20,
        'carrera': "Ingenieria"
    },
    'estudiante2': {
        'nombre': 'Maria',
        'edad': 22,
        'carrera': "Medicina"
    }
}

#Acceder a la edad de Juan
edad_juan = datos['estudiante1']['edad']
print(edad_juan) #salida 20

# Acceder al nombre maria
nombre_Maria = datos['estudiante2']['nombre']
print(nombre_Maria) #salida: Maria

#Par iterar con este diccionario anidado
print("\n\nIteracion con los diccionarios anidados")

for clave_principal, valor_principal in datos.items():
    print(f"Información de {clave_principal}:")
    for clave_anidada, valor_anidado in valor_principal.items():
        print(f"\t{clave_anidada}: {valor_anidado}")


print("hola espero que todo este muy bien con tu madre amigo mio")

