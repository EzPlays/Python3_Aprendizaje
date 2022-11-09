diccionario = {
    1 : "one",
    2 : "too",
    3 : "tree" 
}

diccionario[4] = "four"
resultado = diccionario.get(4,'no existe esta clave')

print(resultado)
print(diccionario)

#obtener valores de un dictionario
for clave,valor in diccionario.items():
    pass
    # print("{0} --> {1}".format(clave,valor))

for clave in diccionario:
    resultado = diccionario.get(clave,"no existe un valor asociado a esta clave o no existe esta clave")
    # print(resultado)

valores = diccionario.values()
print(valores)

keys = diccionario.keys()
print(keys)




