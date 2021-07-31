print('-=' * 20)
print(' ' * 8, '10 TERMOS DE UMA PA')
print('-=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10

while mais != 0 :
    total = total + mais

    while c <= total :
        print('{} -> '.format(termo), end= '')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quer mostrar mais quantos termos?: '))

print('Progressão finalizada com {} termos mostrados!'.format(total))