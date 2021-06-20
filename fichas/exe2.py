notas=[]
nota = int(input('Escreva a nota do aluno (-1 para sair):'))
while nota != -1:
    notas.append(nota)
    nota = int(input('Escreva a nota do aluno (-1 para sair):'))

#calcular media da turma
media = sum(notas)/len(notas)
print(media)
