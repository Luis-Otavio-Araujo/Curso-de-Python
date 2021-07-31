n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva outro número: '))
if (n1 > n2 and n1 > n3):
    print('O número {} é o que tem maior valor!'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número {} é o que tem maior valor!'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O número {} é o que tem maior valor!'.format(n3))
elif n1 < n2 and n1 < n3:
    print('O número {} é o que tem menor valor!'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O número {} é o que tem menor valor!'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O número {} é o que tem menor valor!'.format(n3))
