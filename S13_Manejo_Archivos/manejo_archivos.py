try:
    #Encoding = 'utf8', es para que soporte acentos, tildes, emoticones, etc
    archivo = open('Prueba.txt', 'w', encoding='utf8') #Para abrir un archivo, si no esta creado, se lo crea. El "w" es de escritura el modo
    archivo.write('Agregamos texto\n'#Metodo para escribir un archivo
                  'asi com ahora\n'
                  'todo es facil\n')
except Exception as e: print(f'Ocurrio un error: {e}, {type(e)}')
finally:
    archivo.close()#Metodo para cerrar un archivo
    print('Archivo Cerrado')
    #archivo.write('Agregamos texto\n''pero no se agregara\n') #No se agregara nada, ya que previamente cerramos el file