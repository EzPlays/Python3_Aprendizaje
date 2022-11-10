
tupla = () #tupla vacia
intento_de_tupla = (1) #no es una tupla es un entero, (una tupla contiene multiples datos). (1,2,etc..)
tupla2 = (1,) #si es una tupla con 2 elementos 
tupla3 = (1,2,3) #tupla
tupla4 = tuple([1,2,3,4,5]) #lista combertida a tupla, tambien se puede con un tupla ((1,2,3,4))

print(type(intento_de_tupla))
print(type(tupla))
print(type(tupla2))
print(type(tupla3))
print(type(tupla4))

print(tupla4[3]) #muestra el dato que esta en el indice de la tupla  
print(tupla4[-1]) #muestra el dato que esta en el indice de la tupla a la inversa

tupla4[4] = 10 #las tuplas con inmutables no se pueden remplazar o agregar valores
print(tupla4)

print(dir(tupla)) #funcion que devuelve la lista de atributos válidos de la tupla

del tupla4 #elimina la tupla

print(tupla4)

locations = {
    (343.5464, 454634): 'new york',
    (756.5464, 544646): 'argentina'
} # uso de tuplas en aplicaciones

