suscriptores = set()
salir = False
while not salir:
    print('Buenas, seleccione una opcion')
    print('''\t1.Agregar Suscriptor
            2.Eliminar Suscriptor
            3.Ver lista
            4.Salir''')
    option = int(input('Elija una opcion: ').strip())
    if option == 1:
        suscriptor = input('Por favor, introduzca el email del suscriptor: ').strip()
        if not suscriptor in suscriptores:
            suscriptores.add(suscriptor)
        else:
            print('El suscriptor ya se encuentra en la lista.')
    elif option == 2:
        suscriptor = input('Ingrese el email para ser borrado: ').strip()
        if suscriptor in suscriptores:
            suscriptores.remove(suscriptor)
        else:
            print('El suscriptor no se encuentra en la lista')
    elif option == 3:
        for suscriptor in suscriptores:
            print(suscriptor)
    elif option == 4:
        salir = True
        print('Saliendo...')
else:
    print('Gracias. Vuelva pronto')