#Este es el primer ejemplo sobre la carga de operadores



#operador + 

"""

En Python, la sobrecarga de operadores es una forma de 
*darle un nuevo significado a los operadores 
( +, -, , /, ==, <, >, etc.) 
cuando se usan con objetos creados por ti (clases).

👉 O sea, permite que el mismo operador funcione de manera diferente 
dependiendo del tipo de datos con el que se use.


📌 Métodos especiales de sobrecarga más comunes

__add__(self, other) → +

__sub__(self, other) → -

__mul__(self, other) → *

__truediv__(self, other) → /

__floordiv__(self, other) → //

__mod__(self, other) → %

__pow__(self, other) → **

__eq__(self, other) → ==

__lt__(self, other) → <

__le__(self, other) → <=

__gt__(self, other) → >

__ge__(self, other) → >=



"""

print('El operador + ya está sobrecargado')

print(3 + 4)
print("Hola" + "mundo ")





