num = int(input('Escreva um número: '))
tot = 0
for n in range(1,num + 1) :
    if num % n == 0 :
        print('\033[36m', end= ' ')
        tot += 1
    else :
        print('\033[31m', end= ' ')
    print('{}'.format(n), end= ' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
print('-=' * 20)
if tot == 2 :
    print('Este número é primo!!!')
else :
    print('Este número não é primo!!!')