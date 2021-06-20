#1)

class Disciplina:
    nome = str
    curso = str
    ano = int
    semestre = int
    def __init__(self, nome, curso, ano, semestre):
        self.nome = nome
        self.curso = curso
        self.ano = ano
        self.semestre = semestre

    def imprimir_dados(self):
        print('Nome: ', self.nome)
        print('Curso: ', self.curso)
        print('Ano :', self.ano)
        print('Semestre :', self.semestre)
    
nome = input('Qual o nome? ')
curso = input('Qual o curso? ')
ano = input('Qual o ano? ')
semestre = input('Qual o semestre? ')

Disciplina1 = Disciplina(nome, curso, ano, semestre)
Disciplina1.imprimir_dados()

#2)--------------------------------------------------------------

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

#3---------------------------------------------------------------------------------

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

#4)--------------------------------------------------------------

class Garrafa:
    capacidade = int
    cheia = int
    vazia = int
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.cheia = capacidade
        self.vazia = 0

    def imprimir_dados(self):
        print('Capacidade: ' , self.capacidade)
        print('Quantos litros estão ocupados: ' , self.cheia)
        print('Quantos litros estão livres? ' , self.vazia)
    
    def encher(self,litros):
        self.cheia += litros
        self.vazia -= litros
        if self.cheia == self.capacidade:
            print('Garrafa Cheia')

    def despejar(self,litros):
        self.cheia = self.cheia - litros
        self.vazia = self.vazia + litros

print()

capacidade = int(input('Qual a Capacidade Máxima? '))
litros = Garrafa(capacidade)

despejar = int(input('Quantos litros foram despejados? '))
litros.despejar(despejar)

litros.imprimir_dados()


encher = int(input('Quantos litros foram enchidos? '))
litros.encher(encher)

litros.imprimir_dados()


