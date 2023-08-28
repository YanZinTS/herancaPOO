class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


Produto1 = Livro('Diário de um banana', 47, 'Jeffy Kinney')
Produto2 = Eletronico('Iphone 11', 4000, '20w')

print(Produto1.nome)
print(Produto2.nome)