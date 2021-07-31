from random import randint

n1 = randint(0, 20)
n2 = randint(0, 20)
n3 = randint(0, 20)
n4 = randint(0, 20)
n5 = randint(0, 20)
numeros = (n1, n2, n3, n4, n5)

print(numeros)
print('-=' * 20)
print(f'''O maior número é o {max(numeros)}
O menor número é o {min(numeros)}''')
