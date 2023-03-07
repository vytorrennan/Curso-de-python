from random import randint
numbers = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'The numbers generated were: {numbers}'.replace('(', '').replace(')', ''))
greater = numbers[0]
smaller = numbers[0]
for count in range(0, 5):  # you can also just use max(numbers) and min(numbers) for tuples
    if numbers[count] > greater:
        greater = numbers[count]
    if numbers[count] < smaller:
        smaller = numbers[count]
print(f'The grater number is {greater} and the smallest is {smaller}')
