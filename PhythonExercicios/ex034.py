salario = float(input('Escreva seu salário: R$'))
aumento10 = salario * 10 / 100
aumento15 = salario * 15 / 100
if salario > 1250:
    salario = (salario + aumento10)
    print('A partir de agora você receberá R${:.2f}'.format(salario))
else:
    salario = (salario + aumento15)
    print('A partir de agora você receberá R${:.2f}'.format(salario))