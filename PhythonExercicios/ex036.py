valor = float(input('Qual o valor da casa a venda?: R$'))
salario = float(input('Qual seu salário: R$ '))
tempo = int(input('Pretende pagar em quanto tempo?: '))
prestacao = (valor / (tempo * 12))
if prestacao > salario * 30 / 100:
    print('\033[1;31mEMPRÉSTIMO NEGADO\033[m')
    print('Você pagará em {} anos, R${:.2f} por mês!'.format(tempo, prestacao))
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO\033[m')
    print('Você pagará em {} anos, R${:.2f} por mês!'.format(tempo, prestacao))