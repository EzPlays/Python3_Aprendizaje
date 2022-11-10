lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('a','e','i')
lista2 = [12,43,74,(2,5,6)]

# union,union1,*union2 = lista

union = list(zip(lista,tupla,lista2))
# union = tuple(zip(lista,tupla))
# union = dict(zip(lista,tupla))

print(union)
# print(union1)
# print(union2)


