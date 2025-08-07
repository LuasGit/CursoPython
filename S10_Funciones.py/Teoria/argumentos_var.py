#*args ---> 0 o mas argumentos ---> tupla   
def superheroe(superheroe, nombre, *args_superpoderes): #CON *args hacemos una tupla, la funcion puede aceptar n cantidad de argumentos. Es opcional enviar los argumentos
    print(f'Nombre superheroe: {superheroe}\nNombre: {nombre}\nSuperpoderes: {args_superpoderes}')

superheroe('BATMAN', 'Bruce Wayne','Millonario', 'Excentrico', 'Rico')