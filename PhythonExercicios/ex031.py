distancia = float(input('São quantos Km de viagem? :'))
if distancia <= 200:
    distancia = distancia * 0.50
    print('Você deverá pagar R${:.2f}'.format(distancia))
else:
    distancia = distancia * 0.45
    print('Você deverá pagar R${:.2f}'.format(distancia))