import math

catetoO = float(input('Escreva o tamanho do cateto oposto: '))
catetoA = float(input('Escreva o tamanho do cateto adjascente: '))
hipotenusa = math.hypot(catetoO, catetoA)
print('O valor da hipotenusa é igual a:{:.2f}'.format(hipotenusa))