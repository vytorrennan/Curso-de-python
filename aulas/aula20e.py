def doble(values):
    position = 0
    while position < len(values):
        values[position] *= 2
        position += 1


nums = [3, 6, 3, 7, 5, 9]
doble(nums)
print(nums)
