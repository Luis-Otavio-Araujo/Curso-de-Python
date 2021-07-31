from random import randint


maquina = randint(0, 10)
jogador = int((input('Digite  um  númro de 0  a  10 : ')))
tentativas = 1


while jogador != maquina :
    jogador = int(input('Você errou, digite outro valor: '))
    tentativas += 1

print('-=' * 20)
if jogador == maquina :
    print('Você ganhou e foram nescessárias {} tentativas!'.format(tentativas))


elif tentativas == 1 :
    print('Você ganhou e foram nescessárias {} tentativas!'.format(tentativas))


