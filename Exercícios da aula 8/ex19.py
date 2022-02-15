from random import choice
nome1 = str(input('Qual o nome do primeiro aluno(a): '))
nome2 = str(input('Qual o nome do segundo aluno(a): '))
nome3 = str(input('Qual o nome do terceiro aluno(a): '))
nome4 = str(input('Qual o nome do quarto aluno(a): '))

numero_sorteado = choice([nome1, nome2, nome3, nome4])
print('O nome sortedo foi: {}'.format(numero_sorteado))








