n1 = int(input('Enter a value: '))
n2 = int(input('Enter another value: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
                                                                              #this :.3f here is for limitate the numbers after the point in 3 numbers
print('The sum of this numbers is {} the multiplication is {} the division is {:.3f}'.format(s, m, d), end=' ')#you can use this end='' to don't break a line when go to the next print, and what have in the '' will be the separation of the prints, you can put just a space there too
print(' the entire division is {} the exponentiation is {}'.format(di, e))





                                                                               #this :.3f here is for limitate the numbers after the point in 3 numbers
#print('The sum of this numbers is {} the multiplication is {} the division is {:.3f} the entire division is {} the exponentiation is {}'.format(s, m, d, di, e))

#print('The sum of these numbers is {}'.format(n1+n2)) you can also do this
