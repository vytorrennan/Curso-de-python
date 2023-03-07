from random import randint
from time import sleep


def random_nums(numbers):
    print('Randomizing 5 values of the list: ', end='')
    for c in range(0, 5):
        numbers.append(randint(1, 10))
        sleep(0.5)
        print(nums[c], end=', ')
    print('DONE!')


def summing(numbers):
    total = 0
    for value in numbers:
        if value % 2 == 0:
            total += value
    print(f'Summing the even values of {nums}, we have {total}')


nums = list()
random_nums(nums)
summing(nums)
