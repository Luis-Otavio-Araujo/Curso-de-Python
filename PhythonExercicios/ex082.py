lista = []
impar = []
par = []

while True :
    print('=' * 40)
    num = int(input('Digite um número: '))
    lista.append(num)

    if num % 2 == 0 :
        par.append(num)
    else :
        impar.append(num)

    r = str(input('Quer continar?[S/N]: ')).strip().upper()
    while r != 'S' and r != 'N' :
        r = str(input('Quer continar?[S/N]: ')).strip().upper()

    if r == 'N' :
        print('=' * 40)
        break

print('=' * 40)
print(f'Você digitou os valores {lista}')
print('=' * 40)
print(f'Destes números, os números ímpares são {impar}')
print(f'Destes números, os números pares são {par}')
