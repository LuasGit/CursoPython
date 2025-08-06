salir = False
while not salir:
    print('''***Bienvenido, pana. Escoge una opcion***\n\t1.Crear Cuenta\n\t2.Eliminar Cuenta\n\t3.Salir''')
    option = int(input('option: '))
    if option == 1:
        print('Creando cuenta...')
    elif option == 2:
        print('Eliminando cuenta...')
    elif option == 3:
        print('Saliendo...')
        salir = True
else:
    print('Vuelva pronto')