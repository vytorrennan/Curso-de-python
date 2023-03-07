repetitions = -1
numbers = [0, 12, 15]
answer = 0
_sum = 0
print(len(numbers))
print('if you want to stop the program just type 999 in the program')
while answer != 999:
    numbers.append(answer)
    _sum += answer
    answer = int(input('Enter a integer: '))
    repetitions += 1
print(f'{repetitions} numbers were typed, the sum of all these numbers is {_sum}')
