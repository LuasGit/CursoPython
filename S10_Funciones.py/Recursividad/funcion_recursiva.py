def funcion_recursiva(numero):
    #CASO BASE
    if numero == 1:
        print(numero, end=" ")
    else: #Caso recursivo
        print(numero, end=" ")
        funcion_recursiva(numero - 1)


#Llamando
funcion_recursiva(6)
