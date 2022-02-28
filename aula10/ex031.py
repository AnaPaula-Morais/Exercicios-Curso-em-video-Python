mensagem = '\033[7;36mSeja bem vindo! Será cobrado um valor de R$ 0,50 por km para viagens até 200km'
mensagem2 = ' e R$ 0,45 por km para viagens mais longas.\033[m'
enunciado = str(print(mensagem + mensagem2))
distancia = float(input('\033[1mQual a distância percorrida na sua viagem?\033[m '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('A distância a ser percorrida será {}km e a passagem será de R${:.2f}'.format(distancia, valor))







