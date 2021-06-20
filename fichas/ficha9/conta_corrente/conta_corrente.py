from class_cliente import Cliente


class ContaCorrente:
    numeroConta = int()
    cliente = Cliente
    saldo = float()
    def __init__(self, numeroConta, cliente, saldo):
        self.numeroConta = numeroConta
        self.cliente = cliente
        self.saldo = saldo

    def consultar(self):
        print('Número de Conta: ', self.numeroConta)
        print('Cliente: ', self.cliente.nome)
        print('Saldo: ', self.saldo)

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        print('Saldo: ', self.saldo)

    def levantamento(self, levantamento):
        if saldo > levantamento:
            self.saldo = saldo - levantamento
        else:
            print('Saldo insuficiente!')


