try:
    archivo = open('Prueba.txt', 'r', encoding='utf8') #Si se trabaja en otro lado, es necesario agregar la ruta\\
    #Lee el archivo por completo
    # print(archivo.read())

    #Lee el archivo por caracteres, pero si se ejecuto antes read(), entonces no habra  nada que leer
    # print(archivo.read(4))

    # #Leer lineas completas
    # for linea in archivo:
    #     print(linea)
    # print(archivo.readline())

    #Leer todas las lineas
    # print(archivo.readlines()) #Devuelve todas las lineas en una lista

    #Acceder una linea de la lista
    # print(archivo.readlines()[2])

    #Abrimos un nuevo archivo
    archivo2 = open('Copia.txt', 'a') # CON a de append, se agregara la info al final siempre
    archivo2.write(archivo.read())
except Exception as e: print(f'Ocurrio un error: {e}, {type(e)}')
finally:
    archivo.close()
    archivo2.close()
    print('Se termino el proceso de copia, se cerraron ambos archivos')