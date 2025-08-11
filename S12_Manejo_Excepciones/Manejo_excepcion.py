try:
    a = int(input("Introduce un numero: ").strip())
    b = int(input("Introduce un numero: ").strip())
    print(a/b)
except Exception as e: #ZeroDivisionError, es mas especifico.
    print(f'Ocurrio un error: {e}, {type(e)}')
except TypeError as e: print(f'Ocurrio un error: {e}, {type(e)}')# Las excepciones mas especificas son primero.
except Exception as e: print(f'Ocurrio un error: {e},{type(e)}') #La clase padre de Excepcion debe ir siempre al final.
