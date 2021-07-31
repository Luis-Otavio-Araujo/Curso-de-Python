import math

angulo = float(input('Escreva o ângulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {} tem seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem o tengente de {:.2f}'.format(angulo, tangente))
