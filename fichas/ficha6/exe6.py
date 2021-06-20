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