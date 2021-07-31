soma = 0
for num in range(1,7) :
    num = int(input('Escreva um número: '))
    if num % 2 == 0 :
        soma += num
print('-=' * 20)
print('A soma dos números PARES digitados é: {}'.format(soma))