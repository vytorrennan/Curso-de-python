s = 0
numValues = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        numValues += 1
        s += c
print('\033[35m', end='')
print(f'The sum of all these {numValues} values is {s}')

# É possível resolver esse exercício com uma única linha de código:
#
# print(sum(range(3, 501, 6)))