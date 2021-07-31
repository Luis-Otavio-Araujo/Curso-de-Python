frase = str(input('Escreva a frase: ')).strip().upper()
palavras = frase.split()
junt = (''.join(palavras))
ler = len(junt)
inverso = ''


for c in range(ler - 1, -1, -1 ):
    inverso += junt[c]
print(junt, inverso)
print('-=' * 20)
if junt == inverso :
    print('Temos um palíndromo!!!')
else:
    print('Não temos um palíndromo!!!')

