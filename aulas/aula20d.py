def counter(*num):
    print(type(num))
    i = 0
    for n in num:
        i += 1
        print(i)


counter(3, 6, 3, 7, 5, 9)
counter(3, 3, 7, 9)
