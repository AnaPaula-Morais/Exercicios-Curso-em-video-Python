n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ' )
#coloca-se o {:.3f} para a divisão só ficar com 3 casas após a ,
print('Divisão inteira {} e potência {}'.format(di, e))


