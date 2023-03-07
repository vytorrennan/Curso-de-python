def check_int(text):
    while True:
        try:
            num_int = int(input(text))
        except KeyboardInterrupt:
            print('\nThe user has not entered anything!')
            return 0
        except (TypeError, ValueError):
            print('ERROR: please, enter a valid integer')
        else:
            return num_int


def check_real(text):
    while True:
        try:
            num_real = float(input(text))
        except KeyboardInterrupt:
            print('\nThe user has not entered anything!')
            print(f'You entered the numbers {integer} and 0')
        except:
            print('ERROR: please, enter a valid real number')
        else:
            return num_real


if __name__ == '__main__':
    integer = check_int('Enter a integer: ')
    real = check_real('Enter a real number: ')
    print(f'You entered the numbers {integer} and {real}')
