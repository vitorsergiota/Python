#Exercicio 1
#sem recursividade
import math

def conta_digitos_math(numero):
    contador = int(math.log10(numero)) + 1
    return contador

def conta_digitos_str(numero):
    return len(numero)

#com recursividade
def conta_digitos(numero):
    cont = 1
    if numero < 10:
        return cont
    else:
        numero = numero/10
        cont = cont + conta_digitos(numero)
    return cont

numero = 92345454656
print ('Sem recursividade(math): ', conta_digitos_math(numero))
print ('Sem recursividade(string): ', conta_digitos_str(str(numero)))
print ('Com recursividade: ' , conta_digitos(numero))

#2)---------------------------------------------------

def Ex2():
    #Exercicio 2
    #Escreva uma função contagem_regressiva que recebe um número inteiro positivo n. Quando n for zero, é mostrado no ecrã “Fogo!”, caso contrário mostra o valor de n-1.
        #a. Sem recursividade
        #b. Com recursividade

    #>>> contagem_regressiva (3)
    #3
    #2
    #1
    #Fogo!

    #sem recursividade
    import time

    def contagem_regressiva(numero):
        while numero > 0:
            print(numero)
            time.sleep(1)
            numero = numero -1
        print("Fogo")

    numero = int(input('Qual o número?: '))
    print()
    contagem_regressiva(numero)

    #com recursividade

    print('Com recursividade')

    def contagem_regressiva_rec(numero):
        if numero == 0:
            print ('Fogo!')
        else:
            print(numero)
            time.sleep(1)
            contagem_regressiva_rec(numero -1)
        

    numero = int(input('Qual o número?: '))
    print()
    contagem_regressiva_rec(numero)

Ex2()

#3)---------------------------------------------------

def Ex3():
    #Exercicio 3
    def minmax_com(lista):
        print(max(lista), min(lista))

    def minmax_sem(lista):
        contador = 0
        while contador < len(lista):
            if contador == 0:
                max = lista[contador]
                min = max
            else:
                if max < lista[contador]:
                    max = lista[contador]
                if min > lista[contador]:
                    min = lista[contador]
            contador += 1
        print(max, min)
        

    numeros = [5,6,7,8,9,10]
    print ('Sem recursividade: ')
    minmax_sem(numeros)
    print ('Com recursividade: ')
    minmax_com(numeros)
#ex4--------------------------------------------------
class ContaCorrente:
    num_conta = eval
    nome_cliente = eval
    saldo = eval
    def __init__(self, num_conta, nome_cliente, saldo ):
        self.num_conta = num_conta
        self.nome_cliente = nome_cliente
        self.saldo = saldo

    def imprimir_dados(self):
        print('Número de conta: ', self.num_conta)
        print('Nome de Cliente: ', self.nome_cliente)
        print('Saldo:', self.saldo)

    def depositar(self, deposito):
        self.saldo = saldo + deposito

    def levantar(self, levantar):
        if saldo > levantar:
            self.saldo = saldo - levantar
        else:
            print('Saldo Insuficiente!')

#menu

def menu():
    print("Menu Bancário:")
    print("1-Criar uma conta | 2-Levantamento | 3-Deposito | 4- Informação | 5- Alterar Nome | 9-SAIR ")
    return int(input('Qual a sua escolha ?: '))

opcao=menu()

while opcao != 9:
    if opcao == 1:
        num_conta = int(input('Digite numero da conta: '))
        nome_cliente = str(input('Digite o seu nome: '))
        saldo = int(input('Saldo :'))
        conta1 = ContaCorrente(num_conta, nome_cliente, saldo)
        opcao = menu()
    if opcao == 2:
        levantar = int(input('Quantia a levantar: '))
        conta1.levantar(levantar)
        conta1.imprimir_dados()
        opcao = menu()
    if opcao == 3:
        deposito = int(input('Quantia a depositar: '))
        conta1.depositar(deposito)
        conta1.imprimir_dados()
        opcao = menu()
    if opcao == 4:
        conta1.imprimir_dados()
        opcao = menu()
    if opcao == 5:
        nome_cliente = str(input('Novo Titular: '))
        conta1 = ContaCorrente(num_conta, nome_cliente, saldo)
        conta1.imprimir_dados()
        opcao = menu()
    else:
        print('Escolha errada.Volte a tentar!')
        opcao = menu()