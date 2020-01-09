import os
from database.dao_clientes.cadastroDao import PessoaDao

def consoleApps():
    print('< 1 > - Administração de clientes\n< 2 > - Sair do sistema')
    optionsPrimary = input('\nMe: ')
    os.system('cls')

    if optionsPrimary == "1":
        print('[ 1 ] - Cadastrar novo Cliente\n[ 2 ] - Listar Clientes\n[ 3 ] - Procurar um cliente\n[ 4 ] - Deletar cliente\n[ 5 ] - Voltar')
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

        if optionsPrimary == "4":
            os.system('cls')
            loaded = PessoaDao()
            loaded.del_customer()

        if otherOption == "5":
            os.system('cls')
            consoleApps()

    if optionsPrimary == "2":
        pass