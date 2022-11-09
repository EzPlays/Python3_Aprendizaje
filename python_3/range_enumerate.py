lista = [1,2,2,34,4,5,6,8]


for valor in range(10,21,2):
    print(valor)

for valor in range(len(lista)):
    print(lista[valor])

for valor in enumerate(lista):
    print(valor)

for valor in enumerate(lista,9):
    print(valor)

for posicion,valor in enumerate(lista):
    print('El valor {0} esta en la posicion {1}'.format(valor, posicion))


