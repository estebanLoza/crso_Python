# como no estan en carpeta los demas archivos como
# empleado.py y empresa.py, entonces lo que se hace es solo poner el nombre
# en el video lo pone como "sistema_empleados.empleado"
# lo que se llama 'sistema_empleados' es la carpeta y el punto es el archivo
# el porque el que se llama así.


from empleado import Empleado
from empresa import Empresa


print('**** Sistema de empleados')

# Crear una instancia de una empresa

empresa1 = Empresa("Global Mentoring")

# Creamos algunos empleados

empresa1.contratar_empleado("Juan", "Ventas")
empresa1.contratar_empleado("Maria", "Marketing")
empresa1.contratar_empleado("Ana", "Recursos Humanos")
empresa1.contratar_empleado("Martin", "Recuresos Humanos")

# Obtener el total de objetos de tipo empleado

print(f"El total de empleados: {Empleado.obtener_total_empleados()} ")

# Obtener el numero de empleados en el departamento de ventas


print(
    f"Empleados en el departamento de Ventas: {
        empresa1.obtener_numero_empleados_departamento('Ventas')}"
)


# Mostrar todos los empleados de la empresa1

empresa1.obtener_total_empleados()


# Revisar los archivos empleado.py, empresa y sistema_empleados_app, para saber como es que funciona esto
