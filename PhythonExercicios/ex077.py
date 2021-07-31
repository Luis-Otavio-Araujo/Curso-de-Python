palavras = ('abelha',
            'caramelo',
            'janeiro',
            'sobremesa',
            'uva',
            'comida')

for p in palavras :
    print('\nNa palavra {} temos '.format(p.upper()), end= '')
    for vogais in p :
        if vogais.lower() in 'aeiou' :
            print(vogais.upper(), end= ' ')
