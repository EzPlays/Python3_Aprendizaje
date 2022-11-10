def sumar(numero, suma): return suma + numero


def calcular_suma_elementos(suma=0):
    while True:
        try:
            cantidad_elementos = int(input('ingrese la cantidad de elementos que desea sumar: '))
        except:
            print('la cantidad deben ser solo numeros')
        # except ValueError:
        #     print('la cantidad deben ser solo numeros')
        # except Exception as e:
        #     print(type(e).__name__)
        else:
            break
        # finally:
        #     print('\n-----> Ahora ingrese los numeros para la suma\n')
    while True:
        try:
            for i in range(cantidad_elementos):
                numero = int(
                    input('ingrese el numero que desea agregar a la suma: '))
                suma = sumar(numero, suma)
            print(f'la suma de ls elementos ingresados es: {suma}')
            break
        except:
            print('ingresa solo numeros para hacer la suma')


# calcular_suma_elementos()

def dividir():
    while True:
        try:
            numero = int(input('ingrese un numero: '))
            division = 10/numero
            print(division)
            break
        except ValueError:
            print('inrese un numero no una cadena de texto')
        except ZeroDivisionError:
            print("no se puede realizar una divicion entre 0")
        except Exception as e:
            print(type(e).__name__)

dividir()
