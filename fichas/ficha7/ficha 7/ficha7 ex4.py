'''4. Defina uma classe garrafa que tem como finalidade gerir a quantidade de água
que ela contém. Para isso será necessário:
a. Inicialmente receber a capacidade da garrafa;
b. Mostrar a capacidade total da garrafa;
c. Encher a garrafa com uma determinada quantidade de água, em que se o valor
indicado for superior à capacidade da garrafa, o nível passara a conter a
capacidade da garrafa;
d. Despejar a garrafa de uma determinada quantidade de água, em que se o valor
indicado for superior ao nível da garrafa, o nível passara a conter o valor zero;
e. Mostrar o nível (quantidade de líquido que a garrafa contém)'''

class Garrafa:
    capacidade = int
    cheia = int
    vazia = int
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.cheia = capacidade
        self.vazia = 0

    def imprimir_dados(self):
        print('Capacidade: ' , self.capacidade)
        print('Quantos litros estão ocupados: ' , self.cheia)
        print('Quantos litros estão livres? ' , self.vazia)
    
    def encher(self,litros):
        self.cheia += litros
        self.vazia -= litros
        if self.cheia == self.capacidade:
            print('Garrafa Cheia')

    def despejar(self,litros):
        self.cheia = self.cheia - litros
        self.vazia = self.vazia + litros

print()

capacidade = int(input('Qual a Capacidade Máxima? '))
litros = Garrafa(capacidade)

despejar = int(input('Quantos litros foram despejados? '))
litros.despejar(despejar)

litros.imprimir_dados()


encher = int(input('Quantos litros foram enchidos? '))
litros.encher(encher)

litros.imprimir_dados()