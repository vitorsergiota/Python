notas = [15]
nota = 0
ciclo = 0
while ciclo < 15:
    notas.append(nota)
    
    ciclo = ciclo +1
#calcular media da turma
media = sum(notas)/len(notas)
print(media)