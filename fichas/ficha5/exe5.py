# 5)

notas = []
nomes = []

def cararray():
    contador = 0
    while contador < 20:
        nome = (input('Insira o nome:'))
        nota = int(input('Insira a nota:'))
        nomes.append(nome)
        notas.append(nota)
        contador +=1


def media():
    global med
    contador = 0
    soma = 0
    while contador < 20:
        soma += notas[contador]
        contador +=1
    med = soma / 20
    print("A média é: ",med)

def pos():
    contador = 0
    soma = 0
    while contador < 20:
        if notas[contador] >= med:
            soma += 1
        contador +=1
    print("Nº de alunos com nota acima da media",soma)

def ccc():
    contador = 0
    print("Esta é a média da turma",med)
    print("Este são os alunos com nota acima da média")
    while contador < 20:
       if notas[contador] > med :
            print(nomes[contador])
       contador +=1