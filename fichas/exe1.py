notas=[]
nota = int(input('Escreva a nota do aluno (-1 para sair):'))
while nota != -1:
    if nota > 0 and nota <= 20:
        notas.append(nota)
    nota = int(input('Escreva a nota do aluno (-1 para sair):'))

print(notas)
#calcular media da turma
media = sum(notas)/len(notas)
print(media)
