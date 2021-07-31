valores = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
c = 0

print(f'O valor 9 aparece {valores.count(9)} vezes!')

if 3 in valores :
    print(f'O Valor 3 foi digitado primeiro na posição {valores.index(3) + 1}!')
else:
    print('O valor 3 não foi encontrado')

print(f'Os números pares digitados foram ', end= '')
for par in valores :
    if par % 2 == 0 :
        print(par, end= ' ')