import psycopg2  # importación para usar el postgresql

conexion = psycopg2.connect(
    user='esteban',
    password='m3tr0.elepract',
    host='127.0.0.1',
    port='5432',
    database='test_db'

)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
