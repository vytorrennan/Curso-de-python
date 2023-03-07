import urllib.request

try:
    page = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('You can\'t access the pudim website!')
else:
    print('You can access the pudim website!')
