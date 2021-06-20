

class Cliente:
    nome = str()
    NIF = str()

    def __init__(self, nome1, NIF1):
        self.nome = nome1
        self.NIF = NIF1

    def consultar(self):
        print(self.nome)
        print(self.NIF)

    

   
        