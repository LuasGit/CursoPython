lista_mixta = [1, 'si', 2, 4, 'No']
print(lista_mixta[-2])# Penultima
print(lista_mixta[-1])# Ultima
print(lista_mixta[2])# Tercera
print(lista_mixta)# Toda la lista
print(lista_mixta[0])# Primera

#Modifcamos
lista_mixta [1] = 123
print(lista_mixta [1])

#Agregar un nuevo elemento al final de la lista
lista_mixta.append('Ultima')
print(lista_mixta)

#Agregamos en especifico, sin modificar, recorre a la derecha
lista_mixta.insert(2,'INSERTADO')
print(lista_mixta)

#Eliminando el elemento que proporcionemos (NO ES INDEX)
lista_mixta.remove(1)
print(lista_mixta)

#Removemos por indice
lista_mixta.pop(1)
print(lista_mixta)

#Con delete
del lista_mixta[3]
print(lista_mixta)

#Sublista
sub_lista = lista_mixta[1:3]# EL 3 no se incluye
print(sub_lista)
