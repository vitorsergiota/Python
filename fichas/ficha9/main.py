from conta_corrente import ContaCorrente
from cliente_ficha import ClienteFicha

def menu():
    print()
    print('Banco A - Gestão de Contas')
    print('1- Criar Conta; 2- Depositar; 3- Levantar; 4- Consultar; 5- Remover conta; 9- Sair')
    return int(input('Escolha: '))

opcao = 0
while opcao != 9:
    opcao = menu()
    if opcao == 1:
        numero_de_conta = int(input('Número de Conta: '))
        nomeCliente = str(input('Nome: '))
        nifCliente = int(input('Nif: '))
        moradaCliente = str(input('Morada: '))
        saldo = float(input('Saldo: '))

        cliente1 = ClienteFicha(nomeCliente, nifCliente, moradaCliente)


        conta1 = ContaCorrente(numero_de_conta, saldo, cliente1)

        print("Conta criada com os seguintes dados:")
        conta1.consultar()

    if opcao == 2:
        deposito = float(input('Valor depósito: '))
        conta1.depositar(deposito)

    if opcao == 3:
        levantamento = float(input('Valor levantamento: '))
        conta1.levantamento(levantamento)

    if opcao == 5:
        numero_de_conta = int(input('Número de Conta: '))
        for conta1 in contas:
            if conta1.numeroConta == numero_de_conta:
                conta1.consultar()

    if opcao == 4:
        conta1.consultar()
        