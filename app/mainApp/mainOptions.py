import os
from database.dao_clientes import cadastroDao
from database.dao_clientes.cadastroDao import PessoaDao

def consoleApps():
    print('1 - Cliente\n2 - Obras\n3 - Sair do sistema')
    optionsPrimary = input('\nMe: ')
    os.system('cls')

    if optionsPrimary == "1":
        print('1 - Cadastrar novo Cliente\n2 - Listar Clientes\n3 - Procurar um cliente\n4 - Voltar')
        otherOption = input('\nMe: ')
        if otherOption == "1":
            os.system('cls')
            loaded = PessoaDao()
            loaded.pegar_dados()
            loaded.salvar()
            os.system('cls')
            consoleApps()
        if otherOption == "2":
            os.system('cls')
            loaded = PessoaDao()
            loaded.ler()

        if otherOption == "3":
            os.system('cls')
            loaded = PessoaDao()
            loaded.search_customer()

        if otherOption == "4":
            os.system('cls')
            consoleApps()

    if optionsPrimary == "2":
        print('DAE')

    if optionsPrimary == "3":
        False