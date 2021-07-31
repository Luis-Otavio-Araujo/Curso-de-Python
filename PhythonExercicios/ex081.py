lista = []

while True :
    print('=' * 40)
    n = int(input('Digite um número: '))
    lista.append(n)

    r = str(input('Quer continuar?[S/N]: ')).upper().strip()
    while r != 'S' and r != 'N' :
        r = str(input('Quer continuar?[S/N]: ')).upper().strip()

    if r == 'N' :
        print('=' * 40)
        break

lista.sort(reverse=True)
print(f'Foram digitados na lista {len(lista)} números')
print(f'A lista de valores, ordenada de forma decrescente fica assim: {lista}')

if 5 in lista :
    print('O valor 5 se encontra na lista!')
else:
    print('O valor 5 não foi encontrado!')
