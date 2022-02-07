from typing import NoReturn


numeroMax = int(input(f'Ingrese un numero maximo'))
i = 0
while i <= numeroMax:
    if i % 2 == 0:
        print(f'{i}')
    i+=1