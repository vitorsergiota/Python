A = [[6, 6, 18, 9], 
    [-9, 4, 6, 10],
    [4, 14, 1, 7],
    [0, 4, 22, 9],
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