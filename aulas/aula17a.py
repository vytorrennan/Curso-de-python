num = (2, 5, 9, 1)
#  num[2] = 3
print(num)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)  # choose the position you want to add something
num.pop()  # remove the lest parameter
if 7 in num:
    num.remove(7)  # remove the first "7" it don't remove all of the "7" just the first, but if you want you can use
    # a loop
else:
    print('Don\'t have any seven in num')
print(num)
