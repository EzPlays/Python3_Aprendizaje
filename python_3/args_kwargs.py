# def multiplicar(valor,valor2,valor3):
#     resultado = 1
#     resultado *= valor
#     resultado *= valor2
#     resultado *= valor3
#     return resultado

# print(multiplicar(6,1,2))


# def multiplicar(*args):
#     resultado = 1
#     for i in args:
#         resultado *= i
#     return resultado

# print(multiplicar(6,1,2))

def multiplicar(inicio,*args,**kwargs):
    print(kwargs)
    for i in args:
        inicio *= i
    return inicio

print(multiplicar(8,5,4,3,9,7,num = 50, string= 'a'))