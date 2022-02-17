km = float(input('Quando Km foram percorrido com o carro alugado? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
valor = dias * 60
valor1 = km * 0.15
valor2 = valor + valor1

print('Foram percorridos {} km e o veículo ficou alugado {} dias. '.format(km, dias))
print('O valor a pagar será {:.2f} R$ '.format(valor2))



