phase = input('Enter a phase: ').strip().lower()
if phase.replace(' ', '')[::-1] == phase.replace(' ', ''):
    print(f'That phase \'{phase}\' is a palindrome')
else:
    print(f'That phase \'{phase}\' it\'s not a palindrome')
