'''2. Defina uma classe Pessoa com os seguintes atributos:
- nome, do tipo texto;
- data de nascimento, tipo data;
- altura em metros, tipo float;
A classe deve permitir:
a. Imprimir dados da pessoa
b. Calcular a idade a partir da data de nascimento
c. Verificar se a altura inserida é válida, ou seja, se o valor é superior 0 e inferior
a 2,5 metros. Caso a altura seja inválida, deve ser pedida uma nova altura ao
utilizador e a mesma deve ser guardada no objeto.'''


class Pessoa  :
    nome = str
    data = int
    altura = float
    

    def  __init__(self, nome, data, altura):
     self.nome = nome
     self.data = data
     self.altura = altura 
     

    def  imprimir_dados(self):
         print("Nome: ", self.nome)
         print("Curso: ", self.data)
         print("Ano: ", self.altura)
         


nome = input("Qual é o seu nome? " )
data = input("Qual é a sua data de nascimento? ")


altura = 0

while altura > 2.50 or altura <= 0:
    altura = eval(input('Qual a sua Altura (Em Metros)?: '))
    if altura < 2.50 and altura> 0:
        print('Tem, ' , altura)
    else:
        print('Altura não válida! Preencha novamente!')


pessoa = Pessoa(nome, data, altura)

pessoa.imprimir_dados()


ano_atual = 2021

ano_nasceu = int(input ("Em que ano nasceu?" ))

idade = ano_atual - ano_nasceu 

print("Tem", idade , " anos. ")







