age = int(input('Ingrese su edad: ').strip())
miedo = input('Ingrese si tiene miedo (si/no): ')

permitido = True if age >= 10 else False
if (not (miedo == 'si')) and permitido:
    print('Acceso a la casa del terror. Disfrute su estadia.')
else:
    print('No puedes entrar.')
