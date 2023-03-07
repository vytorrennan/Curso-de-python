matrix = [['0, 0'], ['0, 1'], ['0, 2'],
          ['1, 0'], ['1, 1'], ['1, 2'],
          ['2, 0'], ['2, 1'], ['2, 2']]

# getting the numbers for the matrix
for c in range(0, 9):
    matrix[c] = int(input(f'Enter a number for {matrix[c]}: '))

# showing the matrix
print('=+' * 40)
print(f'[{matrix[0]:^5}] [{matrix[1]:^5}] [{matrix[2]:^5}]\n'
      f'[{matrix[3]:^5}] [{matrix[4]:^5}] [{matrix[5]:^5}]\n'
      f'[{matrix[6]:^5}] [{matrix[7]:^5}] [{matrix[8]:^5}]')
print('=+' * 40)

# Sum of the even numbers
sumEven = 0
for num in matrix:
    if num % 2 == 0:
        sumEven = sumEven + num
print(f'The sum of all even numbers in the matrix is {sumEven}')
# The sum of all the numbers in the third column
print(f'The sum of all the numbers in the third column is {matrix[2] + matrix[5] + matrix[8]}')
# The greater number of the second line
secondLineGreater = matrix[3]
if matrix[4] > secondLineGreater:
    secondLineGreater = matrix[4]
if matrix[5] > secondLineGreater:
    secondLineGreater = matrix[5]
print(f'The greater number of the second line is {secondLineGreater}')
