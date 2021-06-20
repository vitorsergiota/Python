class Estacionamento:
    lotacao = int
    livres = int
    ocupados = int
    def __init__(self, lotacao):
        self.lotacao = lotacao
        self.livres = lotacao
        self.ocupados = 0

    def imprimir_dados(self):
        print('Lotação: ' , self.lotacao)
        print('Quantos lugares Livres?: ' , self.livres)
        print('Quantos lugares Ocupados? ' , self.ocupados)

    def entrada(self,numero_carros):
        self.livres -= numero_carros
        self.ocupados += numero_carros
        if self.livres == 0:
            print('Parque Completo')

    def saida(self,numero_carros):
        self.livres += numero_carros
        self.ocupados -= numero_carros

print()

lotacao = int(input('Qual a Lotação Máxima? '))
parque = Estacionamento(lotacao)

entrada = int(input('Quantos carros entraram? '))
parque.entrada(entrada)

saida = int(input('Quantos carros saíram? '))
parque.saida(saida)

parque.imprimir_dados()