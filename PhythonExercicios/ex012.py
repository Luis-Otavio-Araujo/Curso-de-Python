print('------------------------------------------------')
p = float(input('Qual o preço do produto?:R$'))
d = p * 5 / 100
d2 = p - d
print('------------------------------------------------')
print('O preço do produto com 5% de desconto é :R${:.2f}'.format(d2))
