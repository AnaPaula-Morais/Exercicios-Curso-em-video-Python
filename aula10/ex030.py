numero = int(input('Digite um número qualquer: '))
resultado = numero % 2

if resultado == 0:
    print('O número \033[4;34;40m{} é par\033[m'.format(numero))
else:
    print('O número \033[4;32;40m{} é ímpar\033[m'.format(numero))
