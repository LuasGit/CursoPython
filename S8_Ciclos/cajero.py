salir = False
saldo = 0
while not salir:
    print('''**Banco Sperman**\nDigite una opcion
          1. Consultar Saldo
          2. Depositar
          3. Retirar
          4. Salir''')
    option = int(input('Digite: ').strip())
    if option == 1:
        print(f'Su saldo es: {saldo}')
    elif option == 2:
        deposito = float(input('Introduzca el monto a depositar: ').strip())
        saldo +=deposito
    elif option == 3:
        if saldo > 0:
            retiro = float(input('Introduzca el monto a retirar: ')) 
            if retiro <= saldo:
                saldo -= retiro
            else:
                print(f'No tiene suficientes fondos, solo tiene {saldo}')
        else:
            print('No tiene plata, joven')
    elif option == 4:
        print('Saliendo...')    
        salir = True
    else:
        print('Vuelva a digitar, joven')