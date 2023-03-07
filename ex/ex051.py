firstTerm = int(input('Enter the first term of the PA: '))
reason = int(input('Enter the reason of the PA: '))
print('~' * 42)
print('\033[35mThe first 10 terms of the PA will be this:\033[m')
termNumber = 1
for c in range(firstTerm, firstTerm + (reason * 20), reason):
    print(termNumber, 'term:\033[34m', c, '\033[m')
    termNumber += 1
