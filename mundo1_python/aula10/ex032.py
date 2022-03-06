ano = int(input('\033[40mDigite um ano qualquer para saber se é bissexto:\033[m '))
'''if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Sim o ano {} é bissexto'.format(ano))
        else:
            print('Não o ano {} não é bissexto'.format(ano))
    else:
        print('Sim o ano {} é bissexto'.format(ano))
else:
    print('Não o ano {} não é bissexto'.format(ano))'''  # outra resolução
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
