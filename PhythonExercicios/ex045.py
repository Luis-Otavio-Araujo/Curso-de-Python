import random
import os

ia = ['PEDRA', 'PAPEL', 'TESOURA']
ia2 = random.randint(0, 2)

ganhou = '\033[1;036mVOCÊ VENCEU!!!\033[m'
perdeu = '\033[1;031mVOCÊ PERDEU!!!\033[m'
empate = '\033[1;031mEMPATE!!!\033[m'

print('''Escolha sua jogada:
{}
[0]PEDRA
[1]PAPEL
[2]TESOURA'''.format('-=' * 20))
print('-=' * 20)
jogador = int(input('Sua opção:'))
os.system('cls')

print('-=' * 20)
print('{}     X     {}'.format(ia[ia2], ia[jogador]))
print('-=' * 20)

if ia2 == 0 :
    if jogador == 0 :
        print(empate)

    elif jogador == 1 :
        print(ganhou)
    elif jogador == 2 :
        print(perdeu)
    else:
        print('JOGADA INVALIDA!!!')
elif ia2 == 1 :
    if jogador == 0:
        print(perdeu)
    elif jogador == 1:
        print(empate)
    elif jogador == 2:
        print(ganhou)
    else:
        print('JOGADA INVALIDA!!!')
elif ia2 == 2 :
    if jogador == 0:
        print(ganhou)
    elif jogador == 1:
        print(perdeu)
    elif jogador == 2:
        print(empate)
    else:
        print('JOGADA INVALIDA!!!')