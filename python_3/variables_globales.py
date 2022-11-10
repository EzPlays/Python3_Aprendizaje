canal1 = "var"  # variable global


def mostrar_canal():
    global canal_2 #declarar funcion global
    canal_2 = 'www.google.com'
    # canal3 = 'www.facebook.com'  # variable local funciona solo dentro de la funcion
    # print(canal3)


mostrar_canal()

print(canal_2)

canal_2 = 'sefesfsef'

print(canal_2)

