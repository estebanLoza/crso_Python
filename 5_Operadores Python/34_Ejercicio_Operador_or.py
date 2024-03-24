# En este ejericio se quiere saber si el padre puede ir al juego de su hijo
#para ello usamos este operador logico OR
#ademas de utilizar si dos variables
#vacaciones y diaDescanso


#inciamos suponiendo los valores con false y luego intercambiando un valor a true

vacaciones = True
diaDescanso = False


if vacaciones or diaDescanso:
    print('El padre puede aisistir')
else:
    print('No puede asistir')