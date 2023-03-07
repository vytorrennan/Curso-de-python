def check_num(user_input):
    num = input(user_input)
    while not num.isnumeric():
        print('\033[31mERROR! Enter a valid number.\033[0m')
        num = input(user_input)
    return int(num)


n = check_num('Enter a number: ')
print(f'You entered the number {n}')
