from modulos_pacotes.ex112 import coin
from modulos_pacotes.ex112 import data

price = data.read_money('Enter the price: R$')
coin.resume(price, 35, 22)
