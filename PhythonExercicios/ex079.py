numeros = list()

while True :
    print('=' * 30)
    n = int(input('Escreva um número: '))

    if n not in numeros :
        numeros.append(n)
        print('\033[1;33mNúmero adicionado com sucesso!!!\033[m')
    else:
        print('\033[1;31mNúmero já adicionado, não será adicionado novamente!!!\033[m')

    r = str(input('Quer continuar?[S/N]: ')).upper()
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar?[S/N]: ')).upper()

    if r == 'N' :
        print('=' * 30)
        break

numeros.sort()
print(f'Você digitou os números {numeros}!')