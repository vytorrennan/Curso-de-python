expression = input('Enter the expression, to check the parentheses: ')
parentheses = []

for string in expression:
    if string == '(' or string == ')':
        parentheses.append(string)

for c in range(0, len(parentheses)):
    if '(' in parentheses and ')' in parentheses:
        parentheses.remove('(')
        parentheses.remove(')')
    elif len(parentheses) == 0:
        print('It\'s all ok with the parentheses! :)')
        break
    else:
        print('You have a problem with the parentheses')
        break
