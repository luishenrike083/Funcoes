txt = input('texto: ').split()
n = int(input('digite o número: '))

def print_e(txt, n = 0):
    for i in range(len(txt)):
        print(txt[i], end = ' '*n)

print_e(txt, n)
