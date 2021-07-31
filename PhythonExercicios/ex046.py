import time

for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1)
    if cont == 0 :
        print('BOOOOOM!!!')