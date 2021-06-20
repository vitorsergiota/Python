#adciona numeros até -1 e dá a soma
num = eval(input('Escreva um digito (-1 para terminar): '))
res = 0
while num != -1:
    res = res * 10 + num
    num = eval(input('Escreva um digito (-1 para terminar): '))
print(res)
