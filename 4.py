class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)


GTR_R34 = Carro('Nissan', 'GTR R35', 2005)

XJ6 = Moto('Yamaha', 'XJ6', 2012)

print(GTR_R34.marca)
print(XJ6.modelo)