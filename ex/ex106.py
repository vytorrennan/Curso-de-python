from time import sleep
colors = {'BgDefault': '\033[0;0m',
          'BgGreen': '\033[42m',
          'BgRed': '\033[41m',
          'BgBlue': '\033[46m',
          'BgWhiteLatterBlack': '\033[47m\033[30m'}


def title(title_name, color):
    size = len(title_name) + 20
    print(f'{colors["BgDefault"]}{colors[color]}', end='')
    print('-' * size)
    print(title_name.center(size))
    print('-' * size)
    print(f'{colors["BgDefault"]}', end='')


while True:
    title('PyHELP - HELP SYSTEM', 'BgGreen')
    data = input('Function or library > ')
    sleep(0.5)
    if data.strip().upper() == 'END':
        title('GOODBYE', 'BgRed')
        break
    title(f'ACCESSING COMMAND DATA "{data}"', 'BgBlue')
    sleep(1)
    print(f'{colors["BgWhiteLatterBlack"]}', end='')
    help(data)
