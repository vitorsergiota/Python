#le 3 numeros e indica o maior
num1 = eval (input("Primeiro nº: "))
num2 = eval (input("Segundo nº: "))
num3 = eval (input("Terceiro nº "))
maior = num1
if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3
print("Numero maior :", maior)
