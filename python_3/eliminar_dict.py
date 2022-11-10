dictionario = {
    1: 'one',
    2: 'too',
    3: 'tree'
}

print(dictionario)

# del dictionario[1] #elimina el valor en la posicion indicada del dictionario 
valor_eliminado = dictionario.pop(1) #elimina un valor del dictionario y retorna el valor eliminado

print(valor_eliminado)
dictionario.clear() #elimina todos los valores del dictionario

print(dictionario)
