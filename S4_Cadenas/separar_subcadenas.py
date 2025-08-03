#Separar una cadena en una lista
informacion = 'Alberth Mamani Pita'
nombre_separado = informacion.split()#Por default separar por los espacios en blanco
print(nombre_separado)

#Aqui ya le daremos los parametros a separar
datos = 'Juan, 30, Negro'
lista = datos.split(', ')
print(lista)