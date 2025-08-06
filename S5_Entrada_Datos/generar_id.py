from random import randint
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
anio_nacimiento = input('Ingrese el anio de nacimiento: ')
valor_aleatorio = str(randint(1000,9999))

nom_dig = nombre.strip().upper()[0:2]
ape_dig = apellido.strip().upper()[0:2]
anio_dig = anio_nacimiento.strip()[2:4]
id_unico = nom_dig + ape_dig + anio_dig + valor_aleatorio 
print(id_unico)