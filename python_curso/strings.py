myStr = 'Emanuel'

#formas de concatenar variables a strings
print('my name is ' + myStr)
print(f'my name is {myStr}')
print(f'my name is {0}'.format(myStr))

# metodos
# print(dir(myStr)) 
myStr = 'Hola Mundo'

print(myStr.upper()) #combierte strigs en mayusculas
print(myStr.lower()) #combierte strigs en minusculas
print(myStr.swapcase()) #combierte las mayusculas en minusculas y viseversa
print(myStr.capitalize()) #combierte la primera letra en mayuscula
print(myStr.replace('Hola', 'bye').upper()) # remplasa una parte o todo del string seleccionado, por la nueva frase y la pone en mayuscula
print(myStr.count('l')) #cuenta cuantas veses esta el valor dentro del string 

print(myStr.startswith('Hola')) #devuleve un valor boolean si el valor inicial del string coinside con el valor
print(myStr.endswith('mundo')) #devuleve un valor boolean si el valor final del string coinside con el valor

print(myStr.split('o')) #separa del string el valor dado
print(myStr.find('o')) #busca en el string el valor dado

print(len(myStr)) #devuelve longitud del string
print(myStr.index('l')) #devuelve el indice del string
print(myStr.isnumeric()) #devuleve un valor boolean si el valor es un numero

print(myStr[4]) #busca el caracter del string que se encuentra en la posicion
print(myStr[-1]) #busca el caracter del string que se encuentra en la posicion inversa
