def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print('fin de la cuenta')

    print(f"orden de liberacion {numero}")

cuenta_regresiva(10)

def calcular_factorial(numero):
    if numero > 1: numero *= calcular_factorial(numero - 1)
    return numero

print(calcular_factorial(5))