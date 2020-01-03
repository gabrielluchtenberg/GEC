from app.classes.cadastroCliente.appCadastro_class import *


class PessoaDao:
    def pegar_dados(self):
        self.nome = input('Nome do cliente: ')
        self.idade = input('Idade: ')
        self.telefone = input('Telefone: ')
        print(f'\n{self.nome} cadastrado!')

    def salvar(self):
        with open('cadastro_cliente.txt', 'a') as BancoDados:
            BancoDados.write(f'{self.nome};{self.idade};{self.telefone}\n')


# class Cadastro_clienteDao():
#     def ler(self):
#         with open('cadastro_cliente.txt', 'r') as BancoDados:
#             for l in BancoDados:
#                 banco_dados = l.strip().split(';')
#                 cadastro = Cadastro()
#                 print(Cadastro(cadastro))


cspid = PessoaDao()
cspid.pegar_dados()
cspid.salvar()
