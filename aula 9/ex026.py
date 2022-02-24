frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('Na primeira vez a letra A aparece na posição {}'.format(frase.find('A')+1))
print('Na ultima vez a letra A aparece na posição {}'.format(frase.rfind('A')+1))


