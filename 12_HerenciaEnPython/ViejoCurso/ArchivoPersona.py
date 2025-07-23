#CLASE 114 SOBRE COMO IMPORTAR TODO LOS ARHCIVO


from SobreesctriuraSTR import * #(CON EL * IMPORTAMOS TODOS LOS MODULOS)
    #NOBRE DEL ARHCIVO
persona1 = Persona("Juan", 28)
print(persona1)  #aqui llamara de manera automatica __str__(self): y asi ya no parece la ubicacion de la memoria

empleado = Empleado("Karla", 20, 500)
print(empleado)