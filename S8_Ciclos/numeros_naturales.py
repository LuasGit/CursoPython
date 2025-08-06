rango = int(input('Ingrese un rango: '))
contador = 1
if rango >= 0:
    while contador <= rango:
        print(contador, end=' ')
        contador += 1
else:
    print('No es un numero natural. Ingrese de nuevo')