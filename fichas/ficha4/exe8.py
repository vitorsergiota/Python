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