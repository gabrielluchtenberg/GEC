from app.classes.cadastroCliente.appCadastro_class import Cadastro


class PessoaDao:
    def salvar(self, cadastro: Cadastro):
        with open('dao/pessoa.txt', 'a') as BancoDados:
            BancoDados.write(cadastro.formatacaoDados() + '\n')


class Cadastro_clienteDao:
    def ler(self):
        with open('database/cadastro_cliente.txt', 'r') as BancoDados:
            for l in BancoDados:
                banco_dados = l.strip().split(';')
                cadastro = Cadastro(nome=None, idade=None, telefone=None)
                cadastro.nome = banco_dados[0]
                cadastro.idade = banco_dados[1]
                cadastro.telefone = banco_dados[2]
                print(Cadastro.formatacaoDados(cadastro))
