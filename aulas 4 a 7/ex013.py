salario = float(input('Qual seu salário atual? R$ '))

novo = salario + (salario * 15/100)

print('Seu antigo salário era R${:.2f} com o aumento de 15% agora é R${:.2f}'.format(salario, novo))
