matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c1 in range (0, 3) :
    for c2 in range(0, 3) :
        matriz[c1][c2] = int(input((f'Digite um valor [{c1}, {c2}]: ')))

print('=' * 40)

for c1 in range(0, 3) :
    for c2 in range(0, 3) :
        print(f'[{matriz[c1][c2]:^5}]', end= '')
    print()
print(matriz)