#ficha 4 
#1)

numero = [1,2,3,4,5,6]
for num in numero:
    print(num)

#2)
vetor = []
numero = 0
contadorpar = 0
while numero < 10:
    vetores = int(input("Escreva os numeros :"))
    vetor.append(vetor)
    if ( vetores % 2 ) == 0:
        contadorpar = contadorpar + 1
    numero = numero + 1
print (f"{contadorpar} numeros pares")

# 3)

numero = [1,0,5,-4,3]
print(numero)
soma = sum(numero)
print(soma)
numero.pop(1)
numero.insert(1,50)
print(numero)
soma = sum(numero)
print(soma)

#4)

notas = [15]
nota = 0
ciclo = 0
while ciclo < 15:
    notas.append(nota)
    nota = int(input('Escreva a nota do aluno :'))
    ciclo = ciclo +1
#calcular media da turma
media = sum(notas)/len(notas)
print(media)

# 5)

numeros=[]
contador = 0
while contador < 10:
    numero = int(input('Escreva um vetor:'))
    numeros.append(numero)
    contador = contador + 1
for numero in numeros:
    if numeros.count(numero) > 1:
        print("Numero repetido:", numero)

# 6)

paises = []
contador = 0
while contador < 5:
    pais = str(input("Escreva um país :"))
    paises.append(pais)
    contador = contador +1
print (sorted(paises))

# 7)

A = [[2, 5, 11], 
     [-9, 4, 6],
     [4, 7, 12]]

soma=0
for linha in range(len(A)): # linhas
   for coluna in range(len(A[0])): #colunas
       #soma+=A[linha][coluna]
       soma = soma + A[linha][coluna]

print ("Soma:", soma)

# 8)

A = [[2,5,16,8],
    [3,12,5,10],
    [4,18,8,11],
    [6,7,11,10]]

soma = 0
for linha in range(len(A)): # linhas
   for coluna in range(len(A[0])): #colunas
        #print(A[linha][coluna])    (Ver os números existentes na matriz)
        if A[linha][coluna] > 10:
           soma = soma + 1

print ('Números maiores que 10:', soma)

# 9)

A = [[6, 5, 18, 9], 
    [-9, 4, 6, 10],
    [4, 14, 1, 7],
    [0, 4, 2, 9],
    [1, 6, 2, 16]]

maior = 0
l = 0
c = 0
for linha in range(len(A)): # linhas
   for coluna in range(len(A[0])): #colunas
        #print(A[linha][coluna])    (Ver os números existentes na matriz)
        if A[linha][coluna] > maior:
           maior = A[linha][coluna]
           l = linha
           c = coluna

print ('Maior:', maior)
print ('Linha:', l)
print ('Coluna:', c)
