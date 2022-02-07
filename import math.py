import math
catOpuesto = int(input('Ingrese el valor del cateto opuesto: '))
catAdyacente = int(input('Ingrese el valor del cateto adyacente: '))

hipotenusa = ((catOpuesto**2) + (catAdyacente ** 2))
print(int(math.sqrt(hipotenusa)))