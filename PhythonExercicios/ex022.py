frase = input('Nome completo: ')
print('Seu nome completamente em maiúsculo é: ', frase.upper())
print('Seu nome completamente  minúsculo é: ', frase.lower())
print('Seu nome sem considerar os espaços tem', len(''.join(frase.split())), 'letras')
frase1 = frase.split()
print('Seu primeiro nome tem ', len(frase1[0])  , 'letras')