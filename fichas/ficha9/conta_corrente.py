from cliente_ficha import ClienteFicha


class ContaCorrente:
    numeroConta = int()
    cliente = ClienteFicha
    saldo = float()

    def __init__(self, numeroConta, saldo, cliente):
        self.numeroConta = numeroConta
        self.saldo = saldo
        self.cliente = cliente

    def consultar(self):
        print('Número de Conta: ', self.numeroConta)
        print('Cliente: ', self.cliente.nomeCliente)
        print('Nif: ', self.cliente.nifCliente)
        print('Morada :', self.cliente.moradaCliente)
        print('Saldo: ', self.saldo)

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito

    def levantamento(self, levantamento):
        if self.saldo > levantamento:
            self.saldo = self.saldo - levantamento
        else:
            print('Saldo insuficiente!')
