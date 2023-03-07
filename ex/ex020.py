from random import sample
studant1 = input('Enter the name of the first student: ')
studant2 = input('Enter the name of the second student: ')
studant3 = input('Enter the name of the third student: ')
studant4 = input('Enter the name of the fourth student: ')
order = sample([studant1, studant2, studant3, studant4], k=4)
print('The order will be: {}, {}, {}, {}'.format(order[0], order[1], order[2], order[3]))


# William Rodrigues
# 11 months ago (edited)
# Uma dica que peguei em um dos comentários do exercício anterior: se você quiser saber como faz para ver a
# documentação de uma certa função/módulo pelo PyCharm é só marcar a função/módulo e apertar CTRL + Q.
