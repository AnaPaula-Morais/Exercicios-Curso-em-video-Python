import math
angulo = float(input('Escreva o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print('O ângulo de {}º tem o SEN de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {}º tem o COS de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {}º tem a TAN de {:.2f}'.format(angulo, tangente))

