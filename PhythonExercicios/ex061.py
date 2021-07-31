print('-=' * 20)
print(' ' * 8, '10 TERMOS DE UMA PA')
print('-=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1

while c <= 10 :
    print('{} -> '.format(termo), end= '')
    termo += razao
    c += 1
print('FIM')