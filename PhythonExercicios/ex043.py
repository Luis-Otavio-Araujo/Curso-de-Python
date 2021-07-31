#informações
peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual sua altura?: '))
print('-=' * 20)
#calcular imc
imc = peso / altura ** 2
#falar o estado do paciente
print('Seu IMC é: \033[1;36m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('Você está em: \033[1;36mABAIXO DO PESO!\033[m')
elif imc < 25:
    print('Você está em: \033[1;36mPESO IDEAL!\033[m')
elif imc < 30:
    print('Você está em: \033[1;36mSOBREPESO!\033[m')
elif imc < 40:
    print('Você está em: \033[1;36mOBESIDADE!\033[m')
else:
    print('Você está em: \033[1;36mOBESIDADDE MÓRBIDA!\033[m')
print('-='* 20)
