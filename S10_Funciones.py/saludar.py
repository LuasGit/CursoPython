def saludarPersona(nombre):
    return f"Hola {nombre}, mucho gusto."

def saludarNombreCompleto(nombre, apellido, edad):
    print(f'Hola {nombre} {apellido} con edad {edad}')
print(saludarPersona('Alan'))
saludarNombreCompleto(nombre="Alberth", apellido="Mamani", edad=20)