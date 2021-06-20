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