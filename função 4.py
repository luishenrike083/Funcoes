num = int(input('digite o numero que deseja ser fatorado:'))

def fatorial(num):
    n = num
    for i in range(1, num):
        n *= i
    
    return n

print(fatorial(num))

