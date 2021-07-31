valores = [[],[]]
c = 0

for c in range(0, 7) :
    num = int(input('Digite um número: '))
    if num % 2 == 0 :
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()

print('=' * 40)
print(f'Números pares: {valores[0]}')
print(f'Números ímpares: {valores[1]}')