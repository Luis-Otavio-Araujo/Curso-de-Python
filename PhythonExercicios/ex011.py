largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Serão necessários {:.2f} litros de tinta para pintar {:.2f} m²'.format(tinta,area))