"""
Hacer un programa para calcular la longitud de Circunferencias

"""

import math #ESta es una libreria como la que usas en C (<math.h>), igual funnciones trigo, raiz, exponentes (mas precisa)
""""
 Lo que puedes hacer con esta libreria
### Funciones trigonométricas:
- `math.sin(x)`: Calcula el seno de x (x en radianes).
- `math.cos(x)`: Calcula el coseno de x (x en radianes).
- `math.tan(x)`: Calcula la tangente de x (x en radianes).
- `math.asin(x)`: Calcula el arco seno de x en radianes (devuelve un valor en el rango [-π/2, π/2]).
- `math.acos(x)`: Calcula el arco coseno de x en radianes (devuelve un valor en el rango [0, π]).
- `math.atan(x)`: Calcula el arco tangente de x en radianes (devuelve un valor en el rango [-π/2, π/2]).

### Funciones hiperbólicas:
- `math.sinh(x)`: Calcula el seno hiperbólico de x.
- `math.cosh(x)`: Calcula el coseno hiperbólico de x.
- `math.tanh(x)`: Calcula la tangente hiperbólica de x.
- `math.asinh(x)`: Calcula el arco seno hiperbólico de x.
- `math.acosh(x)`: Calcula el arco coseno hiperbólico de x.
- `math.atanh(x)`: Calcula el arco tangente hiperbólico de x.

### Funciones exponenciales y logarítmicas:
- `math.exp(x)`: Calcula e elevado a la potencia x.
- `math.log(x, base)`: Calcula el logaritmo de x en la base especificada (por defecto, base e).
- `math.log10(x)`: Calcula el logaritmo base 10 de x.
- `math.log2(x)`: Calcula el logaritmo base 2 de x.
- `math.pow(x, y)`: Calcula x elevado a la potencia y.

### Funciones de redondeo y otras operaciones matemáticas:
- `math.ceil(x)`: Redondea x al entero más pequeño no menor que x.
- `math.floor(x)`: Redondea x al entero más grande no mayor que x.
- `math.trunc(x)`: Trunca x eliminando la parte fraccionaria.
- `math.sqrt(x)`: Calcula la raíz cuadrada de x.
- `math.factorial(x)`: Calcula el factorial de x.

### Constantes:
- `math.pi`: El valor de π (pi).
- `math.e`: La base del logaritmo natural, e.

Esto es solo una selección de las funciones y constantes disponibles en la biblioteca `math` de Python. Puedes encontrar más información sobre esta biblioteca y sus funciones en la documentación oficial de Python.
"""


radio = float(input("Ingresa el radio: "))



longitud =  2 * math.pi * radio

print(f"La longitud de la circunferencia es {round(longitud,2)}")


