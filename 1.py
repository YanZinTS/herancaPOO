class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula


Aluno1 = Aluno('Yan', 16, 2479)

print(Aluno1.matricula)