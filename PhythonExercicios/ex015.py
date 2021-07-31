aluguel = int(input('Escreva por quantos dias o carro foi alugado: '))
km = float(input('Escreva quantos KM foram percorridos com o carro alugado:KM'))
total = (60 * aluguel) + (0.15 * km)
print('O preço a pagar é :R${:.2f}'.format(total))