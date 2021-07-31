#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Escreva seu nome: '))
nome = nome.title()
nome = nome.strip()
nomeA = nome.split()
if ('Silva' in nome):
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')





