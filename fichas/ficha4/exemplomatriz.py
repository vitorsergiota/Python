A = [[2, -5, -11, 0],
    [-9, 4, 6, 13],
    [4, 7, 12, -2]]
print(A)


print(A[2][2])
coluna = []
for linha in A:
    coluna.append(linha[2])
    print("3ª coluna =", coluna)
print(A[2])
print(A[0][1])

lines = len(A)
print(lines)
colu = len(A[0])
print(colu)
