#2
numeros = []

def menu():
    print ("Escolha opção :")
    print ("1 - Carregar um array com 10 valores inteiros")
    print ("2 - Mostrar valores do array")
    print ("3 - Somar todas as posições do array")
    print ("4 - Maior valor")
    print ("5 - Valor Minimo")
    print ("6 - Sair")
    return int(input("Qual a opção :"))

def recolhe():
    contador = 0
    while contador < 10:
        numero = int(input('Escreva um vetor:'))
        numeros.append(numero)
        contador = contador + 1

def mostra():
    print(f"Os numeros são : {numeros}")

def somar():
    soma = sum(numeros)
    print(f"A Soma dos numeros é {soma}")

def minimo():
    mini = min(numeros)
    print (f"O numero mais pequeno é {mini}")

def maximo():
    maxi = max(numeros)
    print (f"O numero maior é {maxi}")

opcao = 0
while opcao != 6:
    opcao = menu()
    if opcao == 1:
        recolhe()
    if opcao == 2:
        mostra()
    if opcao == 3:
        somar()
    if opcao == 4:
        minimo()
    if opcao == 5:
        maximo()
        



    





