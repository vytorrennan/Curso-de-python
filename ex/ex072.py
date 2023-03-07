numNames = 'zero', 'one', 'two', 'three', 'four', 'five', ' six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', \
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'

while True:
    userNum = int(input('Enter a number between 0 and 20(if you want stop, enter -1): '))
    if userNum == -1:
        print('program finished')
        break
    while not 0 <= userNum <= 20:
        userNum = int(input('Enter a valid number. Enter a number between 0 and 20: '))
    print(f'You enter a {numNames[userNum]}')
