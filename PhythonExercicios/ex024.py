#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Escreva o nome da cidade:')
cidade = cidade.strip()
cidade = cidade.title()
cidadeA = cidade.split()

if cidadeA[0] == 'Santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')

