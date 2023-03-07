n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
n3 = float(input('Enter another number: '))
organization = [n1, n2, n3]
organization.sort()
print('The lowest number is {}, and the largest is {}'.format(organization[0], organization[2]))


# YOU CAN DO LIKE THIS TOO:
# What is the lowest:
# lowest = a    with that variable you can cutoff one if
# if b < a and b < c:
#     lowest  = b
# if c < a and c< b:
#     lowest = c

# What is the largest:
# largest = a
# if b > a and b > c:
#     largest = b
# if c > a and c> b:
#     largest = c

# print('The lowest number is {}, and the largest is {}'.format(lowest, largest))
