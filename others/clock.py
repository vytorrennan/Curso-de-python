from time import sleep

timePlaying = ''
hours = 0
minutes = 0
seconds = 0
while True:
    sleep(1)
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    print(f'\r{hours}:{minutes}:{seconds}', end='')
