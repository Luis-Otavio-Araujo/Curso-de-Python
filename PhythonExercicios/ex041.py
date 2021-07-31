from datetime import date
nasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nasc
print('-=' * 22)
if idade <= 9:
    print('Você tem {} anos, sua categoria é: \033[1;36mMIRIM\033[m'.format(idade))
    print('-=' * 22)
elif idade > 9 and idade <= 14:
    print('Você tem {} anos, sua categoria é: \033[1;36mINFANTIL\033[m'.format(idade))
    print('-=' * 22)
elif idade > 14 and  idade <= 19:
    print('Você tem {} anos, sua categoria é: \033[1;36mJÚNIOR\033[m'.format(idade))
    print('-=' * 22)
elif idade > 19 and idade <= 25:
    print('Você tem {} anos, sua categoria é: \033[1;36mSÊNIOR\033[m'.format(idade))
    print('-=' * 22)
elif idade > 25:
    print('Você tem {} anos, sua categoria é: \033[1;36mMASTER\033[m'.format(idade))
    print('-=' * 22)