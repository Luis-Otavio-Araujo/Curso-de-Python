idvelho = 0
nmvelho = ''
idade = 0
media = 0
contM = 0
sexo = ''

for p in range(1, 5) :
    print('---- {}° PESSOA ----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('Sexo [M/F]: '))


    if  p == 1 and sexo in 'Mm' :
        idvelho = idade
        nmvelho = nome

    if sexo in 'Mm' and idade > idvelho :
        idvelho = idade
        nmvelho = nome

    if sexo in 'Ff' and idade < 20 :
        contM += 1
print('-=' * 20)

print('A média de idade do grupo é de {} anos'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(idvelho, nmvelho.title()))
print('{} mulheres tem menos de 20 anos.'.format(contM))
