class Cadastro:
    nome = ''
    idade = ''
    telefone = ''

    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def inserindoDados(self):
        self.nome = input('Nome: ')
        self.idade = input('Idade: ')
        self.telefone = input('Telefone: ')

    def formatacaoDados(self):
        return f"{self.nome};{self.idade};{self.telefone}"