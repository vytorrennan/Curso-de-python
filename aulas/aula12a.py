name = str(input('What\'s your name? '))
if name == 'Gustavo':
    print('What a pretty name!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Your name is very popular in the Brazil')
elif name in 'Ana Cláudia Jéssica Juliana':
    print('Beautiful female name!')
else:
    print('Your name is very normal!')
print('Have a nice day, {}!'.format(name))
