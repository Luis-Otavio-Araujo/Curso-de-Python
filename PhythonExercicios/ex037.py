num = int(input('Escreva um número:'))
print('-=' * 20)
print('''Escolha uma da bases de converção:
[1] Converter para \033[36mBINÁRIO\033[m
[2] Converter para \033[36mOCTAL\033[m
[3] Converter para \033[36mHEXADECIMAL\033[m''')
print('-=' * 20)
opcao = int(input('Sua opção:'))
print('-=' * 20)
if opcao == 1:
    print('O número  \033[36m{} \033[m é igual a: \033[36m {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número  \033[36m{} \033[m é igual a: \033[36m {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número  \033[36m{} \033[m é igual a: \033[36m {}'.format(num, hex(num)[2:]))