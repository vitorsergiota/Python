#procura um numero numa lista e diz a posição

def posic(l, n):
    posicao = []
    for i in range( len(l)):
        if(l[i] == n):
            posicao.append(i + 1)
    print(posicao)


posic([2,3,7,4,3], 3)


