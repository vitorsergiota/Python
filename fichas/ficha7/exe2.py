class Pessoa:
    nome = str
    data_de_nascimento = int
    altura_em_metros = float
    
    def __init__(self, nome, data_de_nascimento, altura_em_metros):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.altura_em_metros = altura_em_metros

    def imprimir_dados(self):
        print('Nome: ', self.nome)
        print('Data de Nascimento:' , self.data_mes)
        print('A sua altura (m): ' , self.altura_em_metros)


nome = input('Qual o seu nome : ')
data_de_nascimento = input('Qual a sua data de nascimento :')

altura_em_metros = 0
while altura_em_metros >= 2.5 or altura_em_metros <= 0:
    altura_em_metros = input(float('Qual a altura em metros'))
    if altura_em_metros < 2.5 or altura_em_metros > 0:
        print(f'Tem {altura_em_metros} m')
    else:
        print('Altura inválida! Volte a preencher.')




pessoal = Pessoa(nome, data_de_nascimento, altura_em_metros)
pessoal.imprimir_dados()




