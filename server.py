import os
from app.mainApp.mainOptions import consoleApps

while True:
    os.system('cls')
    if not consoleApps():
        break
