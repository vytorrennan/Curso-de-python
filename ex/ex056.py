name = [0, 0, 0, 0]
age = [0, 0, 0, 0]
sex = [0, 0, 0, 0]
less20F = 0             # less than 20 female
positManAge = []        # Positions Man Ages
manAge = []             # Man Ages

# reading the name, age and sex of 4 peoples
for c in range(1, 5):
    print('=' * 42)
    name[c - 1] = input(f'Enter the name of the {c}ª person: ').strip()
    age[c - 1] = int(input(f'Enter the age of the {c}ª person: ').strip())
    sex[c - 1] = input(f'Enter the sex of the {c}ª person (M or F): ').strip().upper()

print('=*' * 20)
# average of the ages
print(f'The average of the ages is {(age[0] + age[1] + age[2] + age[3]) / 4:.1f}')

# What's the name of the older man
for c in range(0, 4):
    if sex[c] == 'M':
        positManAge.append(c)
for c in range(0, len(positManAge)):
    manAge.append(age[positManAge[c]])
manAge.sort()
for c in range(0, len(positManAge)):
    if age[positManAge[c]] == manAge[len(manAge) - 1]:
        print(f'One of the older man is {name[positManAge[c]]}, he is {manAge[len(manAge) - 1]} years old')

# How many woman is under 20
for c in range(0, 4):
    if sex[c] == 'F':
        if age[c] < 20:
            less20F += 1
print(f'{less20F} woman is under 20')
print('=*' * 20)

''' VERSION OF MY TEACHER - (MORE SIMPLE)


'''