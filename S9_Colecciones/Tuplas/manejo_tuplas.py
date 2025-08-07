#Una tupla es una lista INMUTABLE
tupla = (1,2,3,4,5,5,5,5,2,2,1) #Ya no se le puede agregar nada mas
# tupla[2] = 6
# print(tupla[2]), Lanza error
tupla_void = ()
#Contamos el numero de veces que se repite un elemento dentro
veces = tupla.count(5)
print(f'El numero 5, se repite: {veces}')

#Podemos extraer la posicion de un elemento
index = tupla.index(5)#La primera vez que lo encuentre, ese index se quedara
print(f'El numero 5 esta en la posicion: {index}')
