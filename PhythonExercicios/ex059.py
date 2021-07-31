v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = 0
opcao = 0
nv1 = 0
nv2 = 0

while opcao  != 5 :
    print('\033[36m-=\033[m' * 20)
    print('''Escolha uma opção
[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Novos valores
[5] Sair do programa''')
    opcao = int(input('O que vai querer?:'))
    print('\033[36m-=\033[m' * 20)

    if opcao > 5 or opcao < 1 :
        print('\033[1;31mOPÇÃO INVÁLIDA!!!\033[m')

    if opcao == 1 :
        v3 = v1 + v2
        print('\033[36mA soma desses valores é {}!\033[m'.format(v3))

    elif opcao == 2 :
        v3 = v1 * v2
        print('\033[36mO produto desses valores é {}!\033[m'.format(v3))

    elif opcao == 3 :
        if v1 > v2:
            print('\033[36mO maior valor é {}!\033[m'.format(v1))

        else :
            print('\033[36mO maior valor é {}!\033[m'.format(v2))

    elif opcao == 4 :
        nv1 = int(input('\033[36m1° novo valor:\033[m '))
        v1 = nv1
        nv2 = int(input('\033[36m2° novo valor:\033[m '))
        v2 = nv2