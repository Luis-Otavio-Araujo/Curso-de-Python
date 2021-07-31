m = p = h = 0

while True :

    print(f'''\033[1;36m{'-=' * 20}
         CADASTRE UMA PESSOA
{'-=' * 20}\033[m''')

    idade = int(input('\033[1;32mDigite sua idade: \033[m'))

    if idade > 18:
        p += 1

    sexo = str(input('\033[1;32mSeu sexo[M/F]: \033[m').upper().strip())

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[1;32mSeu sexo[M/F]: \033[m').upper().strip())

    if sexo == 'M' :
        h += 1

    if sexo == 'F' and idade < 20 :
        m += 1

    print('\033[1;36m-=\033[m' * 20)
    opçao = str(input('\033[1;32mQuer continuar?[S/N]: \033[m').upper().strip())

    while opçao != 'S' and opçao != 'N' :
        opçao = str(input('\033[1;32mQuer continuar?[S/N]: \033[m').upper().strip())

    if opçao == 'N' :
        break

print(f'''\033[1;31m{'-=' * 20}
       ANÁLISE DE DADOS DO GRUPO
{'-=' * 20}
Total de pessoas com mais de 18 anos: {p} 
Total de homens cadastrados: {h}
Total de mulheres com menos de 20 anos: {m}\033[m''')
