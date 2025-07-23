# Esto es un ejercicio de proyecto para entender el poo
# elaborando un app para un sistema de empleados

# !!!!!REVISA ESTE Y LA APP DE 'EMPRESA', programas de python

# esto es del 206 al  209

class Empleado:

    # Creacion de un atributo clase (como variable global)
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados += 1
        self.id = Empleado.contador_empleados

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados
