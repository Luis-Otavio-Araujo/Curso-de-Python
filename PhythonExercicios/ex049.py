num = int(input('Quer saber a tabuada de qual número: '))
for cont in range(1, 11) :
    print('{}  x  {:2}  =  {}'.format(num, cont, num * cont))
