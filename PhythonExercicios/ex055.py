maior = 0
menor = 0

for pessoas in range(1,6):
    peso = float(input('\033[36m[{}° pessoa]\033[m Escreva seu peso: Kg'.format(pessoas)))

    if pessoas == 1 :
        maior = peso
        menor = peso

    else :
         if peso > maior :
             maior = peso
         if peso < menor :
            menor = peso

print('-=' * 20)
print('O maior peso lido foi Kg{} e o menor foi Kg{}!'.format(maior, menor))