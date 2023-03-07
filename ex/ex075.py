nine = 0
firstThree = 'no'
even = []

num1 = (input('Enter a number: '))
num2 = (input('Enter another number: '))
num3 = (input('Enter another number: '))
num4 = (input('Enter another number: '))
numbers = (num1, num2, num3, num4)

for c in range(0, 4):
    if '9' in numbers[c]:
        nine += 1
for c in range(0, 4):
    if '3' in numbers[c]:
        firstThree = str(c + 1)+'ª'
        break
for c in range(0, 4):
    if int(numbers[c]) % 2 == 0:
        even.append(c)

print(f'The nine appears {nine} times')
print(f'The first three appears in {firstThree} position')
print(f'The even numbers was: ', end='')
if even:
    for c in range(0, len(even)):
        print(numbers[even[c]], end=', ')
else:
    print('none')
print('That\'s it')
