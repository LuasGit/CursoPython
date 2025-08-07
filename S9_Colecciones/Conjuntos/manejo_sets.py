#En sets (conjuntos) no existen valores repetidos, son mutables
mi_sets = {1,2,2,4,4,5,6}

#Aniadimos con add
mi_sets.add(6)
mi_sets.add(6)#No se agregara ya que esta repetido
mi_sets.add(7)

print(mi_sets)
#Removemos no hay indices
mi_sets.remove(1)
print(f'Set modificado, eliminado 1: {mi_sets}')

for element in mi_sets:
    print(element, end=' ')

#Comprobamos si existe un valor en set
print(f'Existe el valor de 4 en mi_set?: {4 in mi_sets}')

#Longitud del conjunto o set
longitud = len(mi_sets)
print(f'La longitud es: {longitud}')
