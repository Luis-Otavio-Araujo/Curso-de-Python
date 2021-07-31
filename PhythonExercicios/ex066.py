num = c = soma = 0

while True :
    num = int(input('Escreva um número[999 para parar]: '))
    if num == 999 :
        print('-=' * 20)
        break
    c += 1
    soma += num

print(f'Você digitou {c} valores e a soma entre eles é {soma}!')