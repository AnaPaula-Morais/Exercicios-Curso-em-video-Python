nome_completo = str(input('Digite seu nome completo: ')).strip().upper()
nome = nome_completo.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))



