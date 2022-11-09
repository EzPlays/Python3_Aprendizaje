'''
    averiguar si un numero ingresado por consola es par o impar negativo o positivo
'''

print('\t\t\t\t EJERCICIO 1')

num = int(input('ingrese un numero\n'))

#yo
if num < 0:
    if num%2 == 0:
        print('el numero ingresado: ' + str(num) + ' es par negativo')
    else:
        print('el numero ingresado: ' + str(num) + ' es impar negativo')
elif num%2 == 0:
    print('el numero ingresado: ' + str(num) + ' es par positivo')
else:
    print('el numero ingresado: ' + str(num) + ' es impar positivo')


#video
if num%2 == 0:
    print('el numero ingresado es un numero par')
    if num > 0:
        print('el numero tambien es positivo')
    else:
        print('el numero tambien es negativo')
else:
    print('el numero ingresado es un numero impar')
    if num > 0:
        print('el numero tambien es positivo')
    else:
        print('el numero tambien es negativo')

