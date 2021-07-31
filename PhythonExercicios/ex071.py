print('=' * 60)
print('{:^60}'.format('BANCO DO LULU'))
print('=' * 60)

saque = int(input('Quer reitrar quantos reais?: R$'))
cedula = 50
tot = saque
c = 0

while True :

    if tot >= cedula :
        tot -= cedula
        c += 1
    else:
        print(f'Total de {c} cédulas de {cedula} reais!')

        if cedula == 50 :
            cedula = 20

        elif cedula == 20 :
            cedula = 10

        elif cedula == 10 :
            cedula = 1
        c = 0

        if tot == 0 :
            break

print('=' * 60)
print('Volte sempre ao BANCO DO LULU! Tenha um bom dia! ')
