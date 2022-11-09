lista = [1,4,3,2,2,2,2,2,2,2,3,8,9,5]

conjunto = set(lista)

conjunto.add(10)
conjunto.add('aaaa')

print(lista)
print(conjunto)

lista = list(conjunto)

print(lista)

pertenecia = 3 not in conjunto
pertenecia = 3 in conjunto
print(pertenecia)

cadena = "rgdgdrhsefs yfhgyhyg"
conjunto = set(cadena)

print(conjunto)