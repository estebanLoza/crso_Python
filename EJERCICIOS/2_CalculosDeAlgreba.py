Programa para hacer calculos de integrales, matrices

import scipy.integrate as integrate
import scipy.special as special

# Ejemplo primero sobre como usar scipy.integrate as integrate

result = integrate.quad(lambda x: special.jv(2.5, x), 0, 4.5)

print(result)


# Cracionde matrices con listas

m1 = [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]
print(m1)


m1_largoMatriz = len(m1)

for i in range(m1_largoMatriz):
    s = 0
    print(f"esta es la posicion {s+i} {m1[i]}")
