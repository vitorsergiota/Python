#Exercicio 1
#a)

listaCompras = ["manteiga", "arroz", "farinha", "detergente"]
listaCompras.sort(reverse=False)
print(listaCompras)

#b)

def adiciona():
    num = int
    while num != "-1":
        num = str(input("Insira mais itens(-1 para sair) :"))
        listaCompras.append(num)
    listaCompras.pop(-1)
adiciona()
print(listaCompras) 

#c)

x = str(input("Qual o item que procura na lista :"))
if x in listaCompras:
    print("Item encontrado!")
else:
    print("Item não encontrad.") 

#d)
tamanho = len(listaCompras)
print (f"A lista tem {tamanho} itens.")

#Exercicio 2)-----------------------------------------------------------------------------

def lista(l, n):
    if n in l:
        print(f"pertence ({n}, {l})")
    else:
        print(f"não pertence ({n}, {l})")    

lista( [2,3,7], 3 )
lista( [3,4,6], 1 )

#Exercicio 3)-----------------------------------------------------------------------------

def substitui(n, m):
    lista = [2, 3, 7, 4, 3]
    valor = lista.index(n)
    lista[valor] = m
    print(lista)

substitui(3, 0)

#Exercicio 4)-----------------------------------------------------------------------------

def posic(l, n):
    posicao = []
    for i in range( len(l)):
        if(l[i] == n):
            posicao.append(i + 1)
    print(posicao)


posic([2,3,7,4,3], 3)

#Exercicio 5)------------------------------------------------------------------------------

def multiplica():
    mul = ( a * b * c )
    print("Multiplicação :", mul)
def soma():
    som = ( a + b + c )
    print("Soma: ",som)

a = int(input("numero 1: "))
b = int(input("numero 2: "))
c = int(input("numero 3: "))
if a == 0 or b == 0 or c == 0:
    soma()
else:
    multiplica()

#Exercicio 6)-------------------------------------------------------------------------------

respostas = []
cont = 0
print("Responda 'sim' ou 'nao'.")
respostas.append(input("Telefonou para a vitima?\n"))
respostas.append(input("Esteve no local do crime?\n"))
respostas.append(input("Mora perto da vitima?\n"))
respostas.append(input("Tinha algum conflito com a vitima?\n"))
respostas.append(input("Ja trabalhou com a vitima?\n"))
for x in respostas:
    if x == "sim":
        cont +=1
if(cont < 2):
    print("Inocente")
elif(cont < 3):
    print("Suspeita")
elif(cont < 5):
    print("Cumplice")
else:
    print("Culpada")
