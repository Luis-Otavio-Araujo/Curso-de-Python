import datetime

idade = 0
menor = 0
maior = 0

for c in range(0,7) :
    ano = int(input('Digite o ano que você nasceu: '))
    idade = datetime.date.today().year - ano
    if idade <= 18 :
        menor += 1
    else:
        maior += 1

print('-=' * 20)
print('{} pessoas NÃO atingiram a maioridade!'.format(menor))
print('{} pessoas ATINGIRAM a maioridade!'.format(maior))
