listagem = ('lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print(f'''{"=" * 40}
{"LISTAGEM DE PREÇOS":^35}
{"=" * 40}''')

for c in range(0, len(listagem)) :
    if c % 2 == 0 :
        print(f'{listagem[c]:.<30}', end= ' ')
    else :
        print(f'R${listagem[c]:.2f}')
print('=' * 40)