class PessoaDao:
    def pegar_dados(self):
        self.nome = input('Nome do cliente: ')
        self.idade = input('Idade: ')
        self.cpf = input('CPF: ')
        print(f'{self.nome} cadastrada(o)')

    def salvar(self):
        with open('database/dao_clientes/cadastro_cliente.txt', 'a') as BancoDados:
            BancoDados.write(f'Nome: {self.nome};Idade: {self.idade};CPF: {self.cpf}\n')

    def ler(self):
        with open('database/dao_clientes/cadastro_cliente.txt', 'r') as BancoDados:
            for l in BancoDados:
                Cadastro = l.strip().rstrip(';')
                cadastro = Cadastro
                print(cadastro)
