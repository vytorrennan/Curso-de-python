firstTerm = int(input('Enter The first term PA: '))
reason = int(input('Enter the PA reason: '))
times = 0
userTimes = 10
totalTerms = 0

PA = firstTerm
continueLoop = True
while continueLoop:
    print(f'{PA}, ', end='')
    PA = PA + reason

    times += 1
    if times == userTimes:
        print('more?\n')
        userTimes = int(input('How many more PA terms you want to see? use 0 to stop the PA. '))
        times = 0
    if userTimes == 0:
        continueLoop = False
    totalTerms += 1
print(f'\nThe program showed {totalTerms} terms!')
print('Finished')
