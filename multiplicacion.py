
numeroMax = int(input(f'Ingrese un numero maximo: '))
divisor = int(input('Ingresa el divisor: '))
i = 0
while i <= numeroMax:
    if i % divisor == 0:
        print(f'{i}')
    else:
        print('no es divisible ')

    i+=1    