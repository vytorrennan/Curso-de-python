print('\033[35m'+'=' * 70, '\n')
print('\033[35;4mThese are even numbers between 1 and 50:\033[m\033[35m')
for c in range(2, 51, 2):
    print(c, end=' ')
print('\n\n' + '=' * 70)
