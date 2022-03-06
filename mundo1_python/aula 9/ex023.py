'''numero = int(input('Digite um número: '))
n = str(numero)
print('Analisando o número: {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezana: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))








