#UNION
set1 = {1,2,3,1,2,4,1,4}
set2 = {4,5,1,77,88,99,65,44}

set_union = set1.union(set2)#Metodo

union = set1 | set2
print(set_union)
print(union)

#INTERSECCION
intersection = set1 & set2
print(intersection)

#Diferencia
difference = set1 - set2
print(difference)

#Diferencia simetrica
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)