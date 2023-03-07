test = list()
test.append('Gustav')
test.append(40)
guys = list()
guys.append(test[:])
test[0] = 'Marie'
test[1] = 22
guys.append(test[:])
print(guys)
