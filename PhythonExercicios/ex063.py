print('-=' * 20)
print('SEQÊNCIA FIBONACCI')
print('-=' * 20)

n = int(input('Escreva quantos valores você quer: '))
n1 = 0
n2 = 1
n3 = n1 + n2
c = 2

print('-=' * 20)
print('{} -> {}'.format(n1, n3,), end= '')

while c <= n :
    n3 = n1 + n2
    print(' -> {} '.format(n3), end= '')
    n1 = n2
    n2 = n3
    c += 1
print('-> FIM')