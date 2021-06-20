
class Pessoa:
    nome = str
    data_dia = int
    data_mes = int
    data_ano = int
    altura_em_metros = float

    def __init__(self, nome, data_dia, data_mes, data_ano, altura_em_metros):
        self.nome = nome
        self.data_dia = data_dia
        self.data_mes = data_mes
        self.data_ano = data_ano
        self.altura_em_metros = altura_em_metros

    def imprimir_dados(self):
        print('Nome: ', self.nome)
        print(f'Data de Nascimento: {self.data_dia}/{self.data_mes}/{self.data_ano}')
        print('A sua altura (m): ', self.altura_em_metros)


nome = input('Qual o seu nome : ')
data_dia = int(input('Qual o dia de nascimento : '))
data_mes = int(input('Qual o mês de nascimento : '))
data_ano = int(input('Qual o ano de nascimento : '))

altura_em_metros = float(input('Insira a altura: '))
while altura_em_metros <= 0 or altura_em_metros >=2.5:
    altura_em_metros = float(input("Altura invalida, insira uma nova altura :"))

ano_atual = 2021
idade = ano_atual - data_ano
print (f'Tem {idade} anos.')

Pessoa1 = Pessoa(nome, data_dia, data_mes, data_ano, altura_em_metros)
Pessoa1.imprimir_dados()
