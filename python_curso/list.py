demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red','blue','green', 'red']

number_list = list((1,2,3,4,5)) #la funcion list combierte la tupla en una lista

print(number_list) 
print(type(number_list)) 

rangelist = list(range(1,101)) #genera una lista con un rango
print(rangelist) 

print(dir(colors)) #funcion que devuelve la lista de atributos válidos de la lista

print(colors[2]) #muestra el dato que esta en el indice de la lista 
print(colors[-2]) #muestra el dato que esta en el indice de la lista  a la inversa

print('green' in colors) #busca el valor dentro del arreglo y retorna un boolean

print(colors)

colors[2] = 'yellow' #inserta el valor en la posicion asignado

colors.append('black') #agrega el valor en la ultima posicion del la lista y solo acepta un valor

colors.extend(['black','white']) #agrega el valor o los valores mientras esten en una tupla o lista en la ultima 

colors.insert(1,'gold') #inserta el valor en la posicion agregada

colors.insert(len(colors),'black') #inserta el valor segun la longitud de arreglo

print(colors)

colors.pop() #elimina un valor en la lista y lo retorna (se puede insertar un indice)

colors.remove('red') #busca y elimina el valor de la lista (no lo retorna)

# colors.clear() #elimina todos los elementos de la lista

print(colors)

colors.sort() #ordena los valores de la lista alfebeticamente o ala inversa (reverse=True)

indx = colors.index('red') #obtiene el indice del valor de la lista y lo retorna

print(indx)

count = colors.count('red') #obtiene el indice del valor de la lista y lo retorna

print(count)

print(colors)
