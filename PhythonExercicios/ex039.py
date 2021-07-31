from datetime import date
nascimento = int(input('Escreva o ano em que voçê nasceu: '))
print('\033[31m-=\033[m' * 22)
idade = date.today().year - nascimento
if idade < 18:
    tempo = 18 - idade
    print('Você ainda vai se alistar, faltam {} anos!'.format(tempo))
    print('\033[31m-=\033[m' * 22)
elif idade == 18:
    print('Está na hora de se alistar')
    print('\033[31m-=\033[m' * 22)
elif idade > 18:
    tempo = idade - 18
    print('Já se passaram {} anos do tempo determinado!'.format(tempo))
    print('\033[m-=\033[m' * 22)



