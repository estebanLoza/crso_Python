#Este programa recibe los metodos y detalles de las otras apps
#como cuadrado y color y FiguraGeometrica de las apps 


from Cuadrado import Cuadrado


cuadrado1 = Cuadrado(5, 'rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
print(f'Calculo del área cuadrado: {cuadrado1.calcular_area()}')

#Continuación de la clase en el vídeo 232

#MRO = Method Resolution Order
'''
    Es las secuencia en la que python busca un método o atributo dentro de
    una jerarquia de clases, especialemente en casos de herencia multiple.
    


    El MRO es fundamental para:

    1 - Comprender la herencia multiple:
        Permite  comprender cómo python resuelve los conflictos de nombres en la
        herencia múltiple
    
    2 - Debugging:
        Facilita la depuración de código, especialmente en sistemas complejos con
        múltiples capas de herencia

    3 - Desarrollo de código:
        Ayuda a predecir el comportamiento del código, especialmente cuando se trabaja
        con jerarquías de clases complejas

'''

print(Cuadrado.mro())


