lista = [1,2,3,4,5,6,7,2,2,2,2,2,8,9]
tupla = ('sgd','drgdrg','rdgd')

lista_tupla = list(tupla) #combierte una tupla en una lista
tupla_lista = tuple(lista) #combierte una lista en una tupla

print(lista_tupla)


lista.append(15) #inserta el dato en la ultima posicion de la lista
lista.insert(2,30) #inserta en dato en la posicion indicada

print(lista)

borra = lista.remove(15) #elimina el valor agregado en la funcion no retorna el valor eliminado

elimina = lista.pop(3) #elimina el valor en la posicion ingresada en la funcion y retorna el valor eliminado

# lista.clear() #elimina todos los valores de la lista

cantidad = lista.count(2) #cuenta la catidad de valores repetidos dentro de la lista, con el valor de la funcion

norepeat = set(lista)  #elimina los valores duplicados d una lista

print('lista', lista,'\n', 'elimino', elimina, '\n', 'borra', borra, 'cantidad', cantidad, 'sinrepetir', norepeat)


lista2 = ['hola','mundo']

lista.extend(lista2) #une los valores de una lista a otra

nueva_lista = lista.copy()
lista.append('nuevo valor')
lista2.append(nueva_lista)

print(lista)
print(lista2)


