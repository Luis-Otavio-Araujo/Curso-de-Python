sexo = str(input('Qual seu sexo? [M/F]').upper())

while sexo not in 'MF' :
    sexo = str(input('\033[1;31mINVÁLIDO, Qual o seu sexo?:\033[m').upper())
print('-=' * 20)

if sexo == 'M' :
    print('Sexualidade registrada, você é do sexo Masculino!')

elif sexo == 'F' :
    print('Sexualidade registrada, você é do sexo Feminino!')