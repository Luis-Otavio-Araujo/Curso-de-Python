print('-=' * 20)
print(' ' * 9, '10 TERMOS DE UMA PA')
print('-=' * 20)
termo1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo1 + (10 - 1) * razão


for termo1 in range(termo1, décimo + razão, razão) :
    print(termo1, ' ->', end= ' ',)
print('ACABOU!!!')
