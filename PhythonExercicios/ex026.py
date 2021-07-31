#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
palavra = str(input('Escreva uma frase: '))
palavra = palavra.strip()
palavra = palavra.upper()
if 'A' in palavra:
    print('A letra "A" aparece {} vezes!'.format(palavra.count('A')))
    print('Ela aparece primeiro na posição {}!'.format(palavra.find('A') + 1))
    print('Ela aparece por último na posição {}!'.format(palavra.rfind('A') + 1))
else:
    print('Nessa palavra não aparece a letra "A"!')



