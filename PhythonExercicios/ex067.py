num = c = resultado = 0

while True:
    print('-=' * 40)
    num = int(input('Quer saber a tabuada de qual número [Número negativo para parar]: '))

    if num < 0 :
        break

    for c in range(1,11) :
        resultado = c * num
        print(f'{c}     x     {num:} = {resultado}')
