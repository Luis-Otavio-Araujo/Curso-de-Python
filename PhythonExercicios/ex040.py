aluno = str(input('Digite o nome do aluno: '))
print('-=' * 20)
n1 = float(input('Digite a primeira nonta do aluno: '))
print('-=' * 20)
n2 = float(input('Digite a segunda nota do aluno: '))
print('-=' * 20)
media = (n1 + n2) / 2
if media < 5:
    print('\033[1;31mVOCÊ FOI REPROVADO!\033[m')
    print('-=' * 20)
elif media > 5 and media < 6.9:
    print('\033[1;33mVOCÊ ESTÁ DE RECUPERAÇÃO!\033[m')
    print('-=' * 20)
elif media >= 7:
    print('\033[1;36mVOCÊ FOI APROVADO, PARABÉNS!\033[m')
    print('-=' * 20)
