phrase = input('Enter a phase: ').lower().strip()
print("""The phrase have {} times the letter a
The first a is in the position {}
And The last a is in the position {}""".format(phrase.count('a'), phrase.find('a') + 1, phrase.rfind('a') + 1))
