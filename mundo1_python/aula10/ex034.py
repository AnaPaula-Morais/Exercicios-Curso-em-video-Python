salario = float(input('Digite aqui o valor do seu salário: R$ '))
#para salários superiores a 1250.00 reais aumento de 10%, para inferiores ou iguais aumento de 15%

if salario > 1250.00:
    aumento1 = salario + (salario * 0.1)
    print('Salário atual R${:.2f} com aumento de 10% será de R${:.2f}'.format(salario, aumento1))
else:
    aumento2 = salario + (salario * 0.15)
    print('Salário atual R${:.2f} com aumento de 15% será de R${:.2f}'.format(salario, aumento2))





