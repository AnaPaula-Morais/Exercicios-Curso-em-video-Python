print('\033[7m =-=\033[m' *20)
print('\033[0;31m Analizador de triangulos\033[m')
print('\33[7m =-=\033[m' *20)
r1 = float(input('\033[0;32m Primeiro seguimento: \033[m'))
r2 = float(input('\033[0;32m Segundo seguimento: \033[m'))
r3 = float(input('\033[0;32m Terceiro seguimento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima \033[0;31m PODEM FORMAR\033[m triângulo')
else:
    print('Os seguimentos acima \033[0;;40m NÃO PODEM FORMAR\033[m triângulos')


