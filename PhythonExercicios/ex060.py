num = int(input('Quer saber o fatorial de qual número?: '))
c = num
f = 1

print('-=' * 20)
print('Calculando {}! = '.format(num), end= '')

while c > 0 :
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print('{}'.format(f))
