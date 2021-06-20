# simular calculadora
print('Calculadora')
print('1- Soma')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')

opcao = int(input("Seleciona uma opção 1, 2, 3, 4 :"))

if opcao == 1:
    num1 = int(input("1º Número: "))
    num2 = int(input("2º Número: "))
    res = num1 + num2
    print('Resultado: ' , res)

if opcao == 2:
    num1 = int(input("1º Número: "))
    num2 = int(input("2º Número: "))
    res = num1 - num2
    print('Resultado: ' , res)

if opcao == 3:
    num1 = int(input("1º Número: "))
    num2 = int(input("2º Número: "))
    res = num1 * num2
    print('Resultado: ' , res)

if opcao == 4:
    num1 = int(input("1º Número: "))
    num2 = int(input("2º Número: "))
    res = num1 / num2
    print('Resultado: ' , res)

if opcao != [1,2,3,4]:
    print("Opção Inválida!")
    

