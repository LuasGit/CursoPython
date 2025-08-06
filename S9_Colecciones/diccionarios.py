#Crearemos un diccionario clave or key:valor
dictionary = {
    'Name':'Alberth',
    'Age':20,
    'Nacionality':'Bolivian',
    'Height':169
    }

#Accedemos a los elementos del diccionario
print(f'My name is: {dictionary["Name"]}')
print(f'My age is: {dictionary.get("Age")}')
print(f'My height is: {dictionary["Height"]}')

#Modificamos un valor dentro del diccionario
dictionary['Height'] = 170
print(f'My updated height is: {dictionary["Height"]}')

#Agregar al diccionario
dictionary["Social Status"] = 'No money'

#Eliminar la llave o key, esta tambien eliminara el valor asociado
del dictionary['Height']

#otra forma
dictionary.pop('Social Status')
print(f'Dates are: {dictionary}')

#iterando (key, value)
for key, value in dictionary.items():#Se aplica unpacking
    print(f'La llave asociada {key} es {value}')

#Obtenemos los valores
for value in dictionary.values():
    print(f'valores {value}')

#Obtener las keys
for key in dictionary.keys():
    print(f'Llaves: {key}')




