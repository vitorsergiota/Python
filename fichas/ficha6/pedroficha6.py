def Ex1(lista):
    print("Ex1")
    #A
    lista.sort()
    print("Ordem alfabetica",lista)
    #B
    elemento = input("Insira o produto a adicionar")
    lista.append(elemento)
    print("Adicionado")
    #C
    elemento = input("Insira o produto a pesquisar")
    if lista.count(elemento) > 0:
        input("Já tem esse produto na lista")
    else:
        print("Não ta na lista")
    #D
    print("A lista tem ",len(lista)," Produtos")
    print(lista)

def Ex2(lista, elemento):
    print("Ex2")
    contador = lista.count(elemento)
    if contador > 0:
        print("Sim")    
    else:
        print("Não")

def Ex3(lista, velho, novo):
    print("Ex3")
    posicoes = []
    for i in range( len(lista)):
        if(lista[i] == velho):
            posicoes.append(novo)
        else:
            posicoes.append(lista[i])
    print(posicoes)

def Ex4(lista, elemento):
    print("Ex4")
    posicoes = []
    for i in range( len(lista)):
        if(lista[i] == elemento):
            posicoes.append(i + 1)
    print(posicoes)

def Ex5():
    print("Ex5")
    contador = 0
    conta = "multiplicacao"
    soma = 1
    numeros = []
    while contador <3:
        numero = int(input("Insira um numero: "))
        numeros.append(numero)
        if numero == 0:
            conta = "soma"
            soma = 0
        contador +=1
    for x in numeros:
        if conta == "soma":
            soma += x
        else:
            soma *= x
    print("O resultado é: ",soma)
    print("A operação é: ",conta)

def Ex6():
    print("Ex6")
    respostas = []
    contador = 0
    print("Responda 'sim' ou 'nao'.")
    respostas.append(input("Telefonou para a vitima?\n"))
    respostas.append(input("Esteve no local do crime?\n"))
    respostas.append(input("Mora perto da vitima?\n"))
    respostas.append(input("Tinha algum conflito com a vitima?\n"))
    respostas.append(input("Ja trabalhou com a vitima?\n"))
    for x in respostas:
        if x == "sim":
            contador +=1
    if(contador < 2):
        print("Inocente")
    elif(contador < 3):
        print("Suspeita")
    elif(contador <5):
        print("Cumplice")
    else:
        print("Culpada")

Ex1(['manteiga','arroz', 'farinha', 'detergente'])
Ex2([2,3,7],3)
Ex3([2,3,7,4,3],3,0)
Ex4([2,3,7,4,3],3)
Ex5()
Ex6()
