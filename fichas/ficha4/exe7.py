A = [[2, 5, 11], 
     [-9, 4, 6],
     [4, 7, 12]]

soma=0
for linha in range(len(A)): # linhas
   for coluna in range(len(A[0])): #colunas
       #soma+=A[linha][coluna]
       soma = soma + A[linha][coluna]

print ("Soma:", soma)