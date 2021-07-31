#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random as rm
n = int(input('Escreva um número de 1 a 5: '))
n2 = rm.randint(1, 5)
if n == n2:
    print('Você venceu, eu pensei no {}!'.format(n2))
else:
    print('Você perdeu, eu pensei no {}!'.format(n2))
