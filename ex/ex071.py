# variables
fiftyBill = twentyBill = tenBill = oneBill = 0

print('=+' * 27)
print(f'{"SuperBankLie":>33}')
print('=+' * 27)

# collecting the information correctly
money = int(input('Enter how much do you want to withdraw: R$'))

# checking the information according to the parameters and showing the information according to the parameters:
# R$50.00
while money >= 50:
    fiftyBill += 1
    money = money - 50
if fiftyBill != 0:
    print(f'Total of {fiftyBill} bills of R$50')

# R$20.00
while money >= 20:
    twentyBill += 1
    money = money - 20
if twentyBill != 0:
    print(f'Total of {twentyBill} bills of R$20')

# R$10.00
while money >= 10:
    tenBill += 1
    money = money - 10
if tenBill != 0:
    print(f'Total of {tenBill} bills of R$10')

# R$1.00
while money != 0:
    oneBill += 1
    money = money - 1
if oneBill != 0:
    print(f'Total of {oneBill} bills of R$1')

print('~~' * 27)
