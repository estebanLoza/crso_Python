import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Función que representa el sistema
def sistema_oculomotor(y, t, parametros):
    theta, omega = y
    estímulo, constante_muscular = parametros
    dtheta_dt = omega
    domega_dt = -constante_muscular * theta + estímulo
    return [dtheta_dt, domega_dt]

# Parámetros iniciales
estímulo_inicial = 0.5  # Ejemplo de estímulo
constante_muscular = 1.0  # Ejemplo de constante muscular
parametros = [estímulo_inicial, constante_muscular]

# Condiciones iniciales
theta_inicial = 0.0  # Posición inicial del ojo
omega_inicial = 0.0  # Velocidad inicial del ojo
y_inicial = [theta_inicial, omega_inicial]

# Tiempo de simulación
t = np.linspace(0, 10, 200)  # 10 segundos

# Solución de la ecuación diferencial
solucion = odeint(sistema_oculomotor, y_inicial, t, args=(parametros,))

# Gráfica
plt.plot(t, solucion[:, 0], label='Ángulo (θ)')
plt.plot(t, solucion[:, 1], label='Velocidad angular (ω)')
plt.legend()
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.title('Simulación del Sistema Oculomotor')
plt.show()