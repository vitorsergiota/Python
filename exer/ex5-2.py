num = int(input('Escreva um digito:'))
soma=0
while num > 0
    digito = num%10 # obtem algarismo unidades
    num = num // 10 # remove algarismo unidades
    if digito % 2 == 0: #par
        soma = soma + digito
print(soma)
