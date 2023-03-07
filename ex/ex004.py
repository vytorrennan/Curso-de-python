a = input('Enter something: ')
print(
    'the type is: {}\n'
    'is numeric ({})\n' 
    'is a decimal ({})\n'
    'is alphabetical ({})\n'
    'is entirely lower case ({})\n'
    'is entirely upper case ({})\n'
    'is alphanumeric ({})\n'
    'is printable in the screen ({})\n'
    'just have spaces ({})\n'
    'is a digit ({})\n'
    'the first word is uppercase and the others is lowercase ({})'
    .format(type(a), a.isnumeric(), a.isdecimal(), a.isalpha(), a.islower(), a.isupper(), a.isalnum(), a.isprintable(), a.isspace(), a.isdigit(), a.istitle())
)
