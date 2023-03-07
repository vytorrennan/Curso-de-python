from os.path import isfile
from ex.ex113 import check_int
import ex.modulos_pacotes.ex115.funcOptions as funcOptions


def create_archive():
    if isfile('../ex/ex115.txt'):
        pass
    else:
        file = open('../ex/ex115.txt', 'xt')
        file.close()
        print('The ex115.txt file was created successfully!')


def tittle(msg):
    print('+' * 29)
    print(f'{msg:^29}')
    print('+' * 29)


def menu(options):
    tittle('MAIN MENU')
    for c in range(0, len(options)):
        print(f'{c + 1} - {options[c]}')
    print('+' * 29)


def read_opt(options, msg):
    while True:
        user = check_int(msg)
        if user not in range(1, len(options) + 1):
            print('Error, enter a valid option!')
            continue
        return user


def option_selected(msg, num_func):
    func = [funcOptions.show_list, funcOptions.add_person]
    tittle(msg)
    func[num_func]()
