name = 'Guanabara'
print('Hello! Nice to meet you, {}{}{}!!!'.format('\033[4;34m', name, '\033[m'))

# a advance form to do this!
name = 'Guanabara'
colors = {'clean':'\033[m',
          'blue':'\033[34m',
          'yellow':'\033[33m',
          'blackandwhite':'\033[7:30m'}

print('Hello! Nice to meet you, {}{}{}!!!'.format(colors['blackandwhite'], name, colors['clean']))

print(19 // 2)
print(19%2)