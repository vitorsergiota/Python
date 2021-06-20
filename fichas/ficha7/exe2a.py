
class Pessoa:
    nome = str
    data_dia = int
    data_mes = int
    data_ano = int
    altura_em_metros = float
    idade = int

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
        print('Idade: ', self.idade)

    def calcula_idade(self):
        ano_atual = 2021
        self.idade = ano_atual - self.data_ano
        # print(f'Tem {self.idade} anos.')


def pergunta_dados():
    nome = input('Qual o seu nome : ')
    data_dia = int(input('Qual o dia de nascimento : '))
    data_mes = int(input('Qual o mês de nascimento : '))
    data_ano = int(input('Qual o ano de nascimento : '))
    return nome, data_dia, data_mes, data_ano

def pergunta_altura():
    altura_em_metros = float(input('Insira a altura: '))
    while altura_em_metros <= 0 or altura_em_metros >=2.5:
        altura_em_metros = float(input("Altura invalida, insira uma nova altura :"))
    return altura_em_metros


nome, data_dia, data_mes, data_ano = pergunta_dados()
altura_em_metros = pergunta_altura()

pessoa1 = Pessoa(nome, data_dia, data_mes, data_ano, altura_em_metros)
pessoa1.calcula_idade()
pessoa1.imprimir_dados()
