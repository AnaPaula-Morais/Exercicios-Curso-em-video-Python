real = float(input('Quanto dinheiro  você tem na carteira? R$ '))

dolar = real / 5.23
euro = real / 5.96

print('Com R${:.2f} você pode comprar US${:.2f} e eur{:.2f}'.format(real, dolar, euro))




