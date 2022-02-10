altura = float(input('Qual a comprimento da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))

area = altura * largura
print('Sua parede tem dimensão {}x{} e sua área é de {}m2'.format(altura, largura, area))

tinta = area / 2
print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))

