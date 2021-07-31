lista = []
mai = men = 0

for c in range(0, 5) :
    lista.append(int(input('Digite um valor: ')))
    if c == 0 :
        mai = men = lista[c]
    else:
        if lista[c] > mai :
            mai = lista[c]
        if lista[c] < men :
            men = lista[c]

print('=' * 20)
print(lista)
print('=' * 20)

print(f'O maior valor digitado foi o {mai} na posição ', end= '')
for i, v in enumerate(lista) :
    if v == mai :
        print(f'{i + 1}... ', end= '')

print(f'\nO menor valor digitado foi o {men} nas posições ', end= '')
for i, v in enumerate(lista) :
    if v == men :
        print(f'{i + 1}... ', end= '')