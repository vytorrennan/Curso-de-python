from ex.modulos_pacotes import ex115
from time import sleep

# creates the file if it doesn't exist
ex115.create_archive()

while True:
    # MAIN MENU
    options = ['Show the whole list', 'Add a new person', 'Turn off the system']
    ex115.menu(options)

    # INPUT USER
    user = ex115.read_opt(options, 'Your option: ')

    # EXECUTION OF PROGRAM FUNCTIONS
    if user == 1:
        ex115.option_selected('LIST', 0)
    elif user == 2:
        ex115.option_selected('NEW PERSON', 1)
    elif user == 3:
        ex115.tittle('Thanks for using our system')
        sleep(2)
        break
    sleep(2)
