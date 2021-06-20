# ver se é numero par
numero = []
contpar = 0
cont = 0
while cont < 10:
    num = int(input("Numero :"))
    numero.append(num)
    cont +=1
    if num % 2 == 0:
        print("Numero par")
        contpar +=1
print(f"No conjunto {numero} tem {contpar} numeros pares")
