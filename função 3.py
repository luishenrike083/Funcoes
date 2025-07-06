n = []

for i in range(3):
    num = int(input('digite os valores: '))
    n.append(num)

def soma(n):
    resultado = 0
    for i in range(len(n)):
        resultado += n[i]

    return(resultado)

print(soma(n))

