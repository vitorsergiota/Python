# se 3 numeros forem positivos faz multiplicção

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



