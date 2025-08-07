#Variable global
var_global = 0

def incrementar_contador():
    var_local = 0
    global var_global #Estamos utilizando la variable global, esto para usar dentro de funciones
    var_global+=1
    var_local +=1
    print(f'Local: {var_local}')
    print(f'Global: {var_global}')

incrementar_contador()
incrementar_contador()
incrementar_contador()
