import emoji
from playsound import playsound
from time import sleep

print('=-' * 10 + '\033[33m THE FIREWORKS WILL EXPLODE IN... \033[m' + '=-' * 10)
for c in range(10, -1, -1):
    print('\033[33m', c, '\033[m')
    sleep(1)
print(emoji.emojize('=-' * 10+' \033[31m:collision::boom:BOOOOMM:boom::collision:\033[m '+'=-' * 10, use_aliases=True))
playsound('ex046(fireworkExplosion).mp3')
