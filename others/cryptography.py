alfabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z')

# Cesar's cryptography
# reading user's input
word = str(input('Enter the word: ')).upper()
number = int(input('Enter the number of letters forward: '))

# encrypting
for letter in word:
    alfaLetterNum = int(alfabet.index(letter))
    if alfaLetterNum >= 23:
        n = (len(alfabet) - alfaLetterNum) - number
        word = word.replace(letter, alfabet[n])
    else:
        word = word.replace(letter, alfabet[alfaLetterNum + number])
print(f'encrypted is {word}')
