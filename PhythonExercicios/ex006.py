#Crie um algoritimo que leia um número e mostre
#o seu dobro
#o seu triplo
#e sua raiz quadrada

n = int(input('Digite um número:'))
n1 = n * 2
n2 = n * 3
n3 = n **(1/2)
print('============================')
print('============Dobro===========')
print('O dobro desse número é {}'.format(n1))
print('============================')
print('==========Triplo============')
print('O triplo desse número é {}'.format(n2))
print('============================')
print('=======Raiz Quadrada========')
print('A raiz quadrada desse número é {:.2f}'.format(n3))
print('============================')