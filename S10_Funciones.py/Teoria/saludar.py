def saludar_persona(nombre):
    return f"Hola {nombre}, mucho gusto."

def saludar_nombre_completo(nombre, apellido='', edad=0): #apellido y edad estan por default. Nombre si es OBLIGATORIO
    print(f'Hola {nombre} {apellido} con edad {edad}')


print(saludar_persona('Alan'))

#MANDANDO CON ARGUMENTOS Y PARAMETROS (PUEDES INTERCAMBIAR EL ORDEN)
saludar_nombre_completo(nombre="Alberth", apellido="Mamani", edad=20)