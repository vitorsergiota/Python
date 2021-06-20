#4) 
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