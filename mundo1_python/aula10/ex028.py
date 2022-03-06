from random import randint #randomiza um número inteiro
from time import sleep
computador = randint(0, 5) #faz o computador pensar em um número
print('--==--'*10)
print('Vou pensar em um número de 0 a 5, tente adivinhar... ')
print('--==--'*10)
jogador = int(input('Em que número eu pensei? ')) #o jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('PARABÉNS VOCÊ VENCEU!!')
else:
    print('VOCÊ PERDEU! Eu pensei no número {} e não no {}'.format(computador, jogador))








