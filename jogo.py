class Avatar:
    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia
        self.dinheiro = 100

    def mover_direita(self):
        self.energia -= 5
        print('Move para direita...')
        
    def mover_esquerda(self):
        self.energia -= 5
        print('Move para esquerda...')

    def alimenta(self):
        self.energia += 5
        self.dinheiro -= 10
        print('Alimentando:', self.nome)

    def mostra_status(self):
        print('====================')
        print('Nome:', self.nome)
        print('Energia', self.energia)
        print('Dinheiro:', self.dinheiro)
        print('====================')