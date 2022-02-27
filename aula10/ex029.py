velocidade = float(input('Qual a velocidade atual do carro? '))
limite_velocidade = 80


if velocidade <= limite_velocidade:
    print('\033[4;32mParabéns você respeitou o limite de velocidade!!\033[m')
else:
    multa = (velocidade - limite_velocidade) * 7
    print('\033[1;31mVocê ultrapassou o limite de velocidade que era {}km\033[m'.format(limite_velocidade))
    print('\033[1;31mSua multa é R${:.2f}\033[m'.format(multa))

