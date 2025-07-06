n = int(input('digite um número: '))
nome = input('digite uma palavra: ')



def print_e(txt, n = 0):
    for i in range(len(txt)):
        print(txt[i], end=' '*n )



print_e(nome, n)

    
