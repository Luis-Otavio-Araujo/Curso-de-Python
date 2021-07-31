valor = float(input('Qual o valor do produto?: '))

print('-=' * 20)
print('''Escolha a forma de pagamento:
[1] A vista no dinheiro Dinheiro/cheque com 10% de desconto
[2] A vista no cartão com 5% de desconto
[3] Em até 2x no cartão com preço formal
[4] Em até 3x ou mais no cartão com 20% de juros''')
print('-=' * 20)
opcao = int(input('Qual sua escolha?: '))

if opcao > 4 or opcao < 1 :
    print('\033[1;31mOPÇÃO INVÁLIDA!!!\033[m')

elif opcao == 1:

    opcao = valor - (valor * 10 / 100)
    print('Você pagará \033[1;36mR${:.2f}\033[1;36m!'.format(opcao))


elif opcao == 2:

    opcao = valor - (valor * 5 / 100)
    print('Você pagará \033[1;36mR${:.2f}\033[1;36m!'.format(opcao))


elif opcao == 3:

    opcao = valor / 2
    print('Você pagará \033[1;36mR${:.2f}\033[m por mês!'.format(opcao))


elif opcao == 4:

    parcelas = int(input('Quantas parcelas?: '))
    juros = (valor * 20 / 100) / parcelas
    opcao = valor / parcelas
    print('Você pagará \033[1;36mR${:.2f}\033[m por mês \033[1;31mCOM JUROS!\033[m'.format(opcao + juros))
    print('Você pagará ao todo \033[1;36mR${:.2f}\033[m!'.format((opcao + juros) * parcelas))

print('-=' * 20)

