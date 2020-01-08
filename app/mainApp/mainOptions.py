from database.dao_clientes import cadastroDao
from database.dao_clientes.cadastroDao import PessoaDao


def consoleApps():
    print('1 - Cliente\n2 - Obras')
    optionsPrimary = input('Me: ')

    if optionsPrimary == '1':
        print('1 - Cadastrar novo Cliente\n2 - Listar Clientes\n3 - Procurar um cliente')
        otherOption = input('Me: ')
        if otherOption == '1':
            loaded = PessoaDao()
            loaded.pegar_dados()
            loaded.salvar()
        if otherOption == '2':
            loaded = PessoaDao()
            loaded.ler()
        if otherOption == '3':
            loaded = PessoaDao()

    if optionsPrimary == '2':
        print('DAE')

    print(optionsPrimary)