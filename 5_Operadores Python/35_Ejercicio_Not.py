#sobre este ejercicio se hace la practica sobre la logica NOT
# Ademas vamos a invertir la logica del ejercicio anterior donde vemos sobre si el padre puede ir o no ir al juego de su hijo


vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso): # se pone en parentesis ahora si, por que queremos que la respuesta se invierta
    print('Tiene deberes por hacer')
else: #en este caso es verdadera por que desde un inicio estamos invirtiendo la respuesta
    print('Puede asistir al juego')



