import os
from app.mainApp.mainOptions import consoleApps
from database.dao_clientes.cadastroDao import PessoaDao

while True:
    os.system('cls')
    if not consoleApps():
        break
