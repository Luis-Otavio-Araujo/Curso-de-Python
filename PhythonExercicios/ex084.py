princ = []
info = []
maior = 0
menor = 0
c = 0

while True :
    print('=' * 40)

    nome = str(input('Digite seu nome: ')).strip().title()
    info.append(nome)

    peso = float(input('Digite seu peso: Kg '))
    info.append(peso)

    if len(princ) == 0 :
        maior = info[1]
        menor = info[1]
    else:
        if info[1] > maior :
            maior = info[1]

        if info[1] < menor :
            menor = info[1]

    princ.append(info[:])
    info.clear()

    resp = 'x'

    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()

    if resp == 'N' :
        print('=' * 40)
        break

print(f'{len(princ)} pessoas foram cadastradas!')

print(f'As pessoas mais pesadas pesam {maior}Kg. As pessoas são: ', end= '')

for p in princ :

    if p[1] == maior :
        print(f'[{p[0]}]', end= ' ')

print(f'\nAs pessoas mais leves pesam {menor}Kg. As pessoas são: ', end= '')

for p in princ :

    if p[1] == menor :
        print(f'[{p[0]}]', end= ' ')
