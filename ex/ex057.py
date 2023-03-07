wrongAnswer = True

while wrongAnswer:
    gender = input('Enter your gender: (M / F / N-B) ').upper().strip()
    if gender == 'M' or gender == 'F' or gender == 'N-B':
        print('Thank you!')
        wrongAnswer = False
    else:
        print('Please, enter a valid answer!')

'''
YOU CAN DO THIS WAY TOO:

gender = input('Enter your gender: (M / F) ').upper().strip()[0]
while gender not in 'MF':
    gender = input('Please, enter a valid answer: (M / F) ').upper().strip()[0]
print('Thank you!')
'''