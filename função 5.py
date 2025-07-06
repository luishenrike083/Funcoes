n1 = int(input('digite a primeira nota: '))
n2 = int(input('digite a segunda nota: '))
n3 = int(input('digite a terceira nota: '))

def mediaA (n1, n2, n3):
    mediaT = (n1 + n2 + n3) / 3
    return(mediaT)

def mediaP (n1, n2, n3):
    mediat = ((n1 * 2) + (n2 * 4) + (n3 * 6)) / 12
    return(mediat)

def mediaF (mediaA, mediaP):
    mediaa = mediaA(n1, n2, n3)
    mediap = mediaP(n1, n2, n3)
    if mediaa > mediap:
        return mediaa
    else:
        return mediap
    

def conceito (n1, n2, n3):
    mediaf = mediaF(mediaA, mediaP)
    if mediaf <= 100 and mediaf >= 80:
        letra = 'A'
    elif mediaf < 80 and mediaf >= 60:
        letra = 'B'
    elif mediaf < 60 and mediaf >= 40:
        letra = 'C'
    else:
        letra = 'D'

    print(letra)


print('media arítmetica: ', mediaA (n1, n2, n3))
print('media ponderada: ', mediaP (n1, n2, n3))
print('media final: ', mediaF (mediaA, mediaP))
conceito(n1, n2, n3)
