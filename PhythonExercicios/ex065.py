num = soma = media = c = menor = maior = 0
resp = 'S'


while resp == 'S' :
    c += 1
    num = int(input('Digite um valor: '))
    soma += num
    if c == 1 :
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor :
            menor = num
    resp = str(input('Quer continuar?[S/N]').upper())
    print('-=' * 20)

media = soma / c
print('A média entre os valores lidos é {}, o maior valor lido foi {} e o menor foi {}!'.format(media, maior, menor))
