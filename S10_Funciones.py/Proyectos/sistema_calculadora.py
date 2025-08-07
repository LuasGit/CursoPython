def sumar():
    num1 = int(input('Ingrese un numero para sumar: ').strip())
    num2 = int(input('Ingrese otro numero para sumar: ').strip())
    tot= num1 + num2
    while True:
        option = input('Desea sumar otro numero (s/n)?: ').strip()
        if option.lower() == 's':
            num1 = int(input('Ingrese un numero para sumar: ').strip())
            tot+= num1
            continue
        elif option.lower() == 'n':
            break
        else:
            print('Error. Saliendo')
            break
    print(f'El resultado es: {tot}') 
    
def restar():
    num1 = int(input('Ingrese un numero para restar: ').strip())
    num2 = int(input('Ingrese otro numero para restar: ').strip())
    tot= num1 - num2
    while True:
        option = input('Desea restar otro numero (s/n)?: ').strip()
        if option.lower() == 's':
            num1 = int(input('Ingrese un numero para restar: ').strip())
            tot-= num1
            continue
        elif option.lower() == 'n':
            break
        else:
            print('Error. Saliendo')
            break
    print(f'El resultado es: {tot}')  
    
def multiplicar():
    num1 = int(input('Ingrese un numero para multiplicar: ').strip())
    num2 = int(input('Ingrese otro numero para multiplicar: ').strip())
    tot= num1 * num2
    while True:
        option = input('Desea multiplicar otro numero (s/n)?: ').strip()
        if option.lower() == 's':
            num1 = int(input('Ingrese un numero para multiplicar: ').strip())
            tot*= num1
            continue
        elif option.lower() == 'n':
            break
        else:
            print('Error. Saliendo')
            break
    print(f'El resultado es: {tot}')     

def dividir():
    num1 = int(input('Ingrese un numero para dividir: ').strip())
    num2 = int(input('Ingrese otro numero para dividir: ').strip())
    tot= num1 / num2
    while True:
        option = input('Desea dividir otro numero (s/n)?: ').strip()
        if option.lower() == 's':
            num1 = int(input('Ingrese un numero para dividir: ').strip())
            tot/= num1
            continue
        elif option.lower() == 'n':
            break
        else:
            print('Error. Saliendo')
            break
    print(f'El resultado es: {tot}')

def menu():
    salir  = False
    print('Calculadora-Mortadelinha')
    while not salir:
        print(f'''
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Salir''')
        option = int(input("Digite: ").strip())
        if option == 1:
            sumar()
        elif option == 2:
            restar()
        elif option == 3:
            multiplicar()
        elif option == 4:
            dividir()
        elif option == 5:
            salir = True
        else:
            print("xf, digite un valor correcto.")

menu()