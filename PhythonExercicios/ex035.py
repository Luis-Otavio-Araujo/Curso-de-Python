r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))
print('==' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima FORMAM um triângulo!')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')