times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Esport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'''{'-=' * 60}
Os cinco primeiros times são: {times[:5]}
{'-=' * 60}
Os últimos quatro colocados são: {times[-4:]}   
{'-=' * 60}
Times em ordem alfabética: {sorted(times)}
{'-=' * 60}
Em que posição está o time da Chapecoense: {times.index('Chapecoense') + 1}ª posição
{'-=' * 60}''')
