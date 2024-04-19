""""
Imprime las letras del alfabeto de la a la z
las letras se encuentran en el codigo ASCII

"""
 #Se usa la funcion ord('') Devuelve el valor ASCII del caracter dado, ejemplo a == 97
letra = ord('a')

# while letra <= ord('z'):
#     print(f"{chr(letra)} con while")
#     letra+=1

for letra in range(letra, ord('z') + 1):
    print(f"{chr(letra)} con for")  #chr(variable/asci_valor) Devuelve el caracter correspondiente al valor ASCII dado
                                    # 97 == a
