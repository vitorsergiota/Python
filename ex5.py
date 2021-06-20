#Soma somente os numeros pares
x = input("Coloca um numero:")
soma = 0
for y in x:
    y = int(y)
    if y % 2 == 0:
        soma += y
print(soma)
