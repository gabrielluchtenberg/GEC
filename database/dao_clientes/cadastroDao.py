class PessoaDao:
    def pegar_dados(self):
        self.nome = input('Nome do cliente: ')
        self.idade = input('Idade: ')
        self.cpf = input('CPF: ')

    def salvar(self):
        with open('database/dao_clientes/cadastro_cliente.txt', 'a') as BancoDados:
            BancoDados.write(f'{self.nome};{self.idade};{self.cpf}; \n')

    def ler(self):
        with open('database/dao_clientes/cadastro_cliente.txt', 'r') as BancoDados:

            maior = -9999999999
            contador = 0

            for a in BancoDados:
                g = a.strip().split(';')

                if len(g[0]) > maior:
                    maior = len(g[0])

                contador += 1

        with open('database/dao_clientes/cadastro_cliente.txt', 'r') as BancoDados:

            for i in BancoDados:
                i = i.strip().split(';')

                while len(i[0]) < maior:
                    i[0] += " "

                print(f'Nome: {i[0]}\t\t Idade: {i[1]}\t\t CPF: {i[2]}')

            print(f'\nClientes cadastrados: {contador}')
            input('')

    def search_customer(self):
        cpfSearch = input('CPF do cliente: ')
        with open("database/dao_clientes/cadastro_cliente.txt", "r") as BancoDados:

            for i in BancoDados:
                i = i.strip().split(";")
                if cpfSearch == i[2]:
                    print(f"\nNome: {i[0]}\t\t Idade: {i[1]}\t\t CPF: {i[2]}")
                    input("")



