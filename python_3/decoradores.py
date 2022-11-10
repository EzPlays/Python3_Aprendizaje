def decorador(funcion):
    def funcionalidades(*args,**kwargs):
        print('antes de multiplicar')
        resultado = funcion(*args,**kwargs)
        print(resultado)
        print('despues de multiplicar')
    return funcionalidades

@decorador
def multiplicar(num1,num2):
    return num1 * num2


multiplicar(4,2)

