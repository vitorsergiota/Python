from conta_corrente import ContaCorrente
from class_cliente import Cliente

contas = []




def menu():
    print()
    print('Banco A - Gestão de Contas')
    print('1- Criar Conta; 2- Depositar; 3- Levantar; 4- Consultar; 5-Consultar conta; 6- Eliminar conta 9- Sair')
    return int(input('Ação: '))

opcao = 0
while opcao != 9:
    opcao = menu()
    if opcao == 1:
        numero_de_conta = int(input('Número de Conta: ')) 
        nome = str(input('Nome: '))
        NIF = str(input("NIF: "))
        saldo = float(input('Saldo: '))
        cliente1 = Cliente(nome, NIF)

        conta1 = ContaCorrente(numero_de_conta, cliente1, saldo)
        contas.append(conta1)

    if opcao == 2:
        numero_de_conta = int(input('Número de Conta: ')) 
        for conta1 in contas:
            if conta1.numeroConta == numero_de_conta:
                deposito = float(input('Valor depósito: '))
                conta1.depositar(deposito)

    if opcao == 3:
        numero_de_conta = int(input('Número de Conta: ')) 
        for conta1 in contas:
            if conta1.numeroConta == numero_de_conta:
                levantamento = float(input('Valor levantamento: '))
                conta1.levantamento(levantamento)

    if opcao == 4:
        for conta1 in contas:
            conta1.consultar()

    if opcao == 5:
        numero_de_conta = int(input('Número de Conta: ')) 
        for conta1 in contas:
            if conta1.numeroConta == numero_de_conta:
                conta1.consultar()

    if opcao == 6:
        numero_de_conta = int(input('Número de Conta: ')) 
        for conta1 in contas:
            contas.remove



        
    