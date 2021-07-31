#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Escreva a velocidade do carro: '))
print('=-' * 18)
velocidade2 = 80
if velocidade > 80:
    velocidade = (velocidade - velocidade2) * 7
    print('Sua multa será de R${:.2f}'.format(velocidade))
    print('=-' * 18)
else:
    print('Você não será multado!')
    print('=-' * 18)
