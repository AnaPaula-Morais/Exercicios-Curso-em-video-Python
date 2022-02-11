valor = float(input('Qual o valor do produto? R$ '))
desconto = valor - (valor * 5/100)

print('O valor do produto que custava R${:.2f} com 5% de desconto vai custar R${:.2f}'.format(valor, desconto))

