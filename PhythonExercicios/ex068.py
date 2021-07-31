from random import randint

ia= opçao = jog = c = 0

while True :

    ia = randint(1, 5)
    jog = int(input('Escreva um número: '))
    opçao = str(input('Quer par ou ímpar [P/I]: ').upper().strip())

    while opçao != 'I' and opçao != 'P':
        opçao = str(input('\033[1;31mOpcão inválida, digite novamente: \033[m').strip().upper())
        print('-=' * 20)

    if opçao == 'P' and (ia + jog) % 2 == 0 :
        print(f'Você digitou {jog} e a máquina jogou {ia}, o resultado é {ia + jog}')
        print('\033[1;36mVocê ganhou!!!\033[m')

        c += 1

    elif opçao == 'I' and (ia + jog) % 2 == 1 :
        print(f'Você jogou {jog} e a máquina jogou {ia}, o resultado é {ia + jog}')
        print('\033[1;36mVocê ganhou!!!\033[m')

        c += 1

    else :
        print(f'Você jogou {jog} e a máquina jogou {ia}, o resultado é {ia + jog}')
        print('\033[1;31mVocê perdeu!!!\033[m')
        print('-=' * 20)

        break

print(f'\033[1;31mGAME OVER\033[m \nvocê venceu {c} vezes!')
