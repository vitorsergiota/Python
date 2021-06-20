''' 3. Defina a classe estacionamento que pretende simular o funcionamento de um
parque de estacionamento.
a. A classe deve receber um valor inteiro que determina a lotação do parque;
b. Deverá ter um método “saída” que liberta um lugar;
c. Um método “entrada” que ocupa um lugar, e mostra uma mensagem de
“Parque completo”, quando o número de lugares disponíveis for igual a zero;
d. Deve também permitir consultar os lugares disponíveis.'''


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




         