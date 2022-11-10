def primera_funcion(valores):
    print(valores)

    def iterar_valores():

        for i in valores:
            print(i)

        def tercera_funcion():
            print('tercera funcion')
            
        tercera_funcion()

    iterar_valores()
    
        
primera_funcion([1,2,3,4,5])



