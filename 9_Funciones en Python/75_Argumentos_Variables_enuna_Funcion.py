#Argumentos varibles en una funcion


#Definimos una funcion y vamos a iterar una lista de nombres desconocidas
# el * no sabremos la cantidad que sera y con eso ya lo convertira en una tupla

def listarNombres(*nombresdelParametros):
  for nombre in nombresdelParametros:
    print(nombre)

listarNombres('Juan', 'Maria', 'Ernesto')

#Aqui se va a imprimir los otros 2, ya que ahora sabemos que esto
#Agrega en "nombresdelParametros"

listarNombres('Luara', 'Carlos')