class Forma():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


class Retangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)

    def calcular_area(self):
        area = self.largura * self.altura
        return area


class Triangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)

    def calcular_area2(self):
        area2 = (self.largura * self.altura) / 2
        return area2


Medidas = Retangulo(4, 2)
print(Medidas.calcular_area())

Medidas = Triangulo(4, 2)
print(Medidas.calcular_area2())