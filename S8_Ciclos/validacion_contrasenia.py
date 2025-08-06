password = input('Digite una contrasenia: ').strip()
while len(password) < 6:
    password = input('Por favor, la contrasenia debe ser de al menos 6 caracteres. Digite nuevamente: ').strip()
else:
    print('Su contrasenia fue creada con exito.')


user = None
while not user:
    user = input('Ingrese un usuario: ')
else:
    print('Muchas Gracias')

