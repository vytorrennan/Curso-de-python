from ex.ex113 import check_int


def show_list():
    file = open('../ex/ex115.txt', 'rt')
    file_text = file.read().split()
    for c in range(0, len(file_text)):
        if c % 2 == 0:
            print(f'{file_text[c]:<27}', end='')
        if c % 2 == 1:
            print(file_text[c])
    file.close()


def add_person():
    file = open('../ex/ex115.txt', 'at')
    name = input('Name: ')
    age = check_int('Age: ')
    file.write(' \n' + name + ' ' + str(age))
    file.close()
    print(f'{name} added to the list!')
