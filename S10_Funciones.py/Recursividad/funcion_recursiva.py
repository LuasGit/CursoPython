def funcion_recursiva(numero):
    #CASO BASE
    if numero == 1:
        print(numero, end=" ")
    else: #Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=" ")


#Llamando
funcion_recursiva(6)
