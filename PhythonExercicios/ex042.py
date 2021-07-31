r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))
print('-=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima \033[1;36mFORMAM\033[m um triângulo!')
    print('-=' * 20)
    if r1 == r2 == r3:
        print('Seu triângulo é: \033[1;30mEQUILÁTERO\033[m')
        print('-=' * 20)
    elif r1 != r2 != r3 != r1:
        print('Seu triângulo é: \033[1;30mESCALENO\033[m!')
        print('-=' * 20)
    else:
        print('Seu triângulo é: \033[1;30mISÓSCELES\033[m')
        print('-=' * 20)
else:
    print('Os segmentos \033[1;31mNÃO FORMAM\033[m um triângulo!')
    print('-=' * 20)