matrix = [['0, 0'], ['0, 1'], ['0, 2'],
          ['1, 0'], ['1, 1'], ['1, 2'],
          ['2, 0'], ['2, 1'], ['2, 2']]
for c in range(0, 9):
    matrix[c] = int(input(f'Enter a number to {matrix[c]}: '))
print('=+' * 40)
print(f'[{matrix[0]:^5}] [{matrix[1]:^5}] [{matrix[2]:^5}]\n'
      f'[{matrix[3]:^5}] [{matrix[4]:^5}] [{matrix[5]:^5}]\n'
      f'[{matrix[6]:^5}] [{matrix[7]:^5}] [{matrix[8]:^5}]')
