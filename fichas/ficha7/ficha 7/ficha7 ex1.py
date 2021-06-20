'''1. Defina uma classe Disciplina com os seguintes atributos:
- nome, tipo texto;
- curso, tipo texto;
- ano, tipo inteiro;
- semestre, tipo inteiro;
A classe deve permitir:
a. Imprimir dados da disciplina
b. No final, deve pedir os dados da disciplina ao utilizador e guardar esses
dados no objeto disciplina. Deve também mostrar o resultado ao utilizador,
para que esta possa verificar se os dados introduzidos estão corretos.'''


class Disciplina  :
    nome = str
    curso = str 
    ano = int
    semestre = str


    def  __init__(self, nome, curso, ano, semestre):
     self.nome = nome
     self.curso = curso 
     self.ano = ano 
     self.semestre = semestre

    def  imprimir_dados(self):
         print("Nome: ", self.nome)
         print("Curso: ", self.curso)
         print("Ano: ", self.ano)
         print("Semestre: ", self.semestre)



nome = input("Qual é o seu Disciplina? " )
curso = input("Qual é o seu curso? ")
ano = input("Qual é o seu ano? ")
semestre = input("Qual é o seu semestre? ")

disciplina = Disciplina(nome, curso, ano, semestre)

disciplina.imprimir_dados()

    