cont = total = menor = c = 0
barato = ''

print(f'''\033[1;36m{'-=' * 20}
             LOJA DO LUISÃO''')

while True :
    print('\033[1;36m-=\033[m' * 20)
    nome = str(input('\033[1;33mNome do produto: \033[m').strip())
    preco = float(input('\033[1;33mPreço: \033[m').strip())

    if preco > 1000 :
        c +=1

    cont += 1
    total += preco

    if cont == 1 :
        menor = preco
        barato = nome
    else:
        if preco < menor :
            menor = preco
            barato = nome

    opcao = str(input('\033[1;33mQuer continuar[S/N]?: \033[m').strip().upper())

    while opcao != 'S' and opcao != 'N' :
        opcao = str(input('\033[1;33mQuer continuar[S/N]?: \033[m').strip().upper())

    if opcao == 'N' :
        break

print(f'''\033[1;31m{'-=' * 20}
        FIM DA COMPRA
{'-=' * 20}
Total da compra: \033[1;36mR${total:.2f}\033[m
\033[1;31mProdutos acima de R$1000,00: \033[1;36m{c} produtos\033[m''')
print(f'\033[1;31mProduto mais barato: \033[1;36m{barato} que custou R${menor:.2f}\033[m')