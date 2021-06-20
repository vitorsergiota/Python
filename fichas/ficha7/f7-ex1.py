class Disciplina:
    nome = str()
    curso = str()
    ano = int()
    semestre = int()

    def __init__(self, novo_nome, novo_curso, novo_ano, novo_semestre):
        self.nome = novo_nome
        self.curso = novo_curso
        self.ano = novo_ano
        self.semestre = novo_semestre
    
    def imprimir(self):
        print("Nome:", self.nome)
        print("Curso:", self.curso)

nome_ins = input("Insira o nome da disciplina:")
curso_ins = input("Insira o curso da disciplina:")
ano_ins = int(input("Insira o ano da disciplina:"))
semestre_ins = int(input("Insira o semestre da disciplina:"))

prog = Disciplina(nome_ins, curso_ins, ano_ins, semestre_ins)
prog.imprimir()

bd = Disciplina("Base de Dados", "CTESP Ciberseguranca", 1, 2)
bd.imprimir()
