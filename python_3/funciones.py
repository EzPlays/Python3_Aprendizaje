#funcion sin valores

# def sumar():
#     print('sumar 2 numeros')
#     num1 = int(input('ingrese primer numero\n'))
#     num2 = int(input('ingrese segundo numero\n'))
#     suma = num1 + num2
#     print('resultado', suma)

# for i in range(3):
#     sumar()


#funcion con valores

# print('sumar 2 numeros')

# def sumar2(num1, num2):
#     suma = num1 + num2
#     print('resultado', suma)

# for i in range(3):
#     num1 = int(input('ingrese primer numero\n'))
#     num2 = int(input('ingrese segundo numero\n'))
#     sumar2(num1,num2)


#funcion retornando valores

print('sumar 2 numeros')

def sumar2(num1, num2):
    suma = num1 + num2
    return suma
    
for i in range(2):
    num1 = int(input('ingrese primer numero\n'))
    num2 = int(input('ingrese segundo numero\n'))
    resultado = sumar2(num1,num2) #el valor retornado puede almacenarse en una variable
    print('resultado:', resultado)
    print('resultado:', sumar2(num1,num2)) #el valor retarnado puede usarse con la misma funcion
