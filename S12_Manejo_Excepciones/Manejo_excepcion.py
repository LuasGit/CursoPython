from numeros_identicos_excepcion import NumerosIdenticos
result = None
try:
    a = int(input("Introduce un numero: ").strip())
    b = int(input("Introduce un numero: ").strip())
    if a == b:
        raise NumerosIdenticos('Numeros identicos') #Con raise lanzamos una excepcion de la clase creada. NO solamente arroja la clase creada, puee ser cualquiera
    result = a / b
except Exception as e: #ZeroDivisionError, es mas especifico.
    print(f'Ocurrio un error: {e}, {type(e)}')
except ValueError as e: print(f'Ocurrio un error: {e}, {type(e)}')
except TypeError as e: print(f'Ocurrio un error: {e}, {type(e)}')# Las excepciones mas especificas son primero.
except Exception as e: print(f'Ocurrio un error: {e},{type(e)}') #La clase padre de Excepcion debe ir siempre al final.
else:
    print('No se mando ninguna excepcion.')
finally:
    print('SIEMPRE SE EJECUTARA ESTA LINEA.')
print('COntinuando...')
print(f'Resultado: {result}')