n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))


menor = 0


def menor (n1, n2, n3):
    if n1 < n2 and n1 <n3:
        menor = n1
    elif n2 < n1 and n2 <n3:
        menor = n2
    else:
        menor = n3

    return (menor)


numT = menor(n1, n2, n3)


print(numT)
