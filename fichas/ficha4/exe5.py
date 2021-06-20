#Procura um numero duplicado
numeros=[]
contador = 0
while contador < 10:
    numero = int(input('Escreva um vetor:'))
    numeros.append(numero)
    contador = contador + 1
for numero in numeros:
    if numeros.count(numero) > 1:
        print("Numero repetido:", numero)

