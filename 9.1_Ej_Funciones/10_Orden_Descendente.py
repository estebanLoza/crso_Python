
def sumar(num1, num2, num3):
    
    #sI NUM1 ES MENOR
    if num1 <= num2 and num1 <= num3:
        if num2 <= num3:
            print(f"{num1}, {num2}, {num3}")
        else:
            print(f"{num1},{num3}, {num2}")
    
    #SI NUM2 ES MENOR
    if num2 <= num1 and num2 <= num3:
        if num1 <= num3:
            print(f"{num2}, {num1}, {num3}")
        else:
            print(f"{num2}, {num3}, {num1}")
        
    #Si NUM3 es MENOR

    if num3 <= num1 and num3 <= num2:
        if num1 <= num2:
            print(f"{num3}, {num1}, {num2}")
        else:
            print(f"{num2},{ num2}, {num1}")
        




num1 = int(input("Numero1: "))
num2 = int(input("Numero2: "))
num3 = int(input("Numero3: "))

sumar(num1, num2, num3)