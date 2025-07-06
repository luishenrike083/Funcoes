num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
num3 = int(input('digite o terceiro número: '))

def menor(num1, num2, num3):
    menor = 0
    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num1 and num2 < num3:
         menor = num2
    elif num3 < num1 and num3 < num2:
         menor = num2
    return menor


menornum= menor(num1, num2, num3)
print(menornum)

