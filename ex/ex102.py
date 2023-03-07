def factorial(num=0, show=False):
    """
    -> It Calculate the factorial of a number
    :param num: The number that will be used
    :param show: (optional)To show or not every step of the calculation
    :return: The factorial of the number num
    """
    print('-' * 27)
    result = list()
    total = num
    for c in range(num - 1, 0, -1):
        total *= c
        if show:
            result.append(str(c))
            if c == 1:
                result.insert(0, str(num))
                result = ' X '.join(result)
                result += ' = '
                result += str(total)
    if show:
        return result
    else:
        return total


help(factorial)
print(factorial(5, True))
