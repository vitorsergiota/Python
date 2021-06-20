#1)

def cinco(num):
    if num == 5:
        print("True")
    else:
        print("False")

num = int(input("Qual o numero:"))
cinco(num)

#2--------------------------------------------------------------------

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

# 3)-----------------------------------------------------------------------

def asterisco():
    num = int(input("Quantos asteriscos :"))
    contador = 0
    while contador < num:
        print( end = "*") 
        contador = contador + 1

asterisco()

# 4) ------------------------------------------------------------------------

def menu():
    print ("Máquina de Calcular")
    print ("Escolha a opção:")
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Sair.")
    return int(input("Qual a opção: "))

def soma():
    num1 = int(input("Primeiro numero : "))
    num2 = int(input("Segundo numero : "))
    soma = num1 + num2
    print (f"A some de {num1} + {num2} = {soma}")

def subtracao():
    num1 = int(input("Primeiro numero : "))
    num2 = int(input("Segundo numero : "))
    sub = num1 - num2
    print (f"A subtração de {num1} - {num2} = {sub}")

def multiplicacao():
    num1 = int(input("Primeiro numero : "))
    num2 = int(input("Segundo numero : "))
    mult = num1 * num2
    print (f"A multiplicação de {num1} * {num2} = {mult}")

def divisao():
    num1 = int(input("Primeiro numero : "))
    num2 = int(input("Segundo numero : "))
    div = num1 / num2
    print (f"A divisão de {num1} / {num2} = {div}")

opcao = 0
while opcao != 5:
    opcao = menu()
    if opcao == 1:
        soma()
    if opcao == 2:
        subtracao()
    if opcao == 3:
        multiplicacao()
    if opcao == 4:
        divisao()

#5) ------------------------------------------------------------------

notas = []
nomes = []

def cararray():
    contador = 0
    while contador < 20:
        nome = (input('Insira o nome:'))
        nota = int(input('Insira a nota:'))
        nomes.append(nome)
        notas.append(nota)
        contador +=1


def media():
    global med
    contador = 0
    soma = 0
    while contador < 20:
        soma += notas[contador]
        contador +=1
    med = soma / 20
    print("A média é: ",med)

def pos():
    contador = 0
    soma = 0
    while contador < 20:
        if notas[contador] >= med:
            soma += 1
        contador +=1
    print("Nº de alunos com nota acima da media",soma)

def ccc():
    contador = 0
    print("Esta é a média da turma",med)
    print("Este são os alunos com nota acima da média")
    while contador < 20:
       if notas[contador] > med :
            print(nomes[contador])
       contador +=1
