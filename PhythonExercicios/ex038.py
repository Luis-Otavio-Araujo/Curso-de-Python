n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('\033[34m-=\033[m' * 22)
if n1 > n2 :
    print('O número {} é o que tem maior valor!'.format(n1))
elif n2 > n1:
    print('O número {} é o que tem maior valor!'.format(n2))
elif n1 < n2:
    print('O número {} é o que tem menor valor')
else:
    print('Não existe valor maior, os dois são iguais!')
print('\033[34m-=\033[m' * 22)