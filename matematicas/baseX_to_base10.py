class colors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

numeroBx = input('Ingresa un numero: ')
base = int(input(f'¿En que base esta el numero {numeroBx}?: '))
respuesta = 0
#print(str(numeroBx)[0])
if len(str(numeroBx)) == 3:
    respuesta = (int(numeroBx[0])*(base**2))+(int(numeroBx[1])*(base))+(int(numeroBx[2]))
    print(f'El numeral {colors.OK}{numeroBx}{colors.RESET} en base {colors.FAIL}{base}{colors.RESET}\n es equivalente a {colors.OK}{respuesta}{colors.RESET} en base {colors.FAIL}10{colors.RESET}.')

