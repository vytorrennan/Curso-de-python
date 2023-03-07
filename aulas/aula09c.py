phrase = 'Course in Video Python'
print(phrase.count('o'))

phrase = 'Course in Video Python'
print(phrase.upper().count('O'))

phrase = 'Course in Video Python'
print(len(phrase))

phrase = '       Course in Video Python       '
print(len(phrase))

phrase = '       Course in Video Python       '
print(len(phrase.strip()))

phrase = 'Course in Video Python'
print(phrase.replace('Python', 'Android'))
print(phrase)      # a string is immutable
phrase = phrase.replace('Python', 'Android')  # but you can redefine them
print(phrase)

phrase = 'Course in Video Python'
print('Course' in phrase)

phrase = 'Course in Video Python'
print(phrase.find('Video'))

phrase = 'Course in Video Python'
print(phrase.lower().find('video'))

phrase = 'Course in Video Python'
print(phrase.split())

phrase = 'Course in Video Python'
divided = phrase.split()
print(divided[0])

phrase = 'Course in Video Python'
divided = phrase.split()
print(divided[2][3])