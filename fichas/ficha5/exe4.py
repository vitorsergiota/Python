# 4)

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

