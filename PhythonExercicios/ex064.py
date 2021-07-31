num = int(input('Digite um número[999 para parar]: '))
c = 0
soma = 0

while num != 999 :
    soma += num
    c += 1
    num = int(input('Digite um número[999 para parar]: '))
print('-=' * 20)

print('Você digitou {} valores antes de encerrar o programa e a soma entre eles é {}!'.format(c, soma))
