import psycopg2  # importación para usar el postgresql

'''
    Esta es la forma más básica que podemos 
    hacer para crear una conexion con la base de datos
'''


conexion = psycopg2.connect(
    user='esteban',
    password='m3tr0.elepract',
    host='127.0.0.1',
    port='5432',
    database='test_db'

)


# Aquí estamos cerrando manualmente cursor con la conexion
# de base de datos

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)


cursor.close()
conexion.close()
