name = input('Enter your full name: ')
name.strip()
print('Your name capital letters is {}'.format(name.upper()))
print('Your name in lower case is {}'.format(name.lower()))
print('Your name has {} letters'.format(len(name) - name.count(' ')))
print('Your first name has {} letters'.format(len(name[:name.find(' ')])))

# Vytor Rennan Alves Carvalho
