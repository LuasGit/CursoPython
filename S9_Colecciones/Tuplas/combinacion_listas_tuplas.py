#COMBINAREMOS LISTTAS Y TUPLAS
#DEFINIMOS UNA LISTA CON TUPLAS DE PRODUCTOS
productos = [
    ('P001', 'Camisa', 20.0),
    ('P002', 'Jeans', 30.0),
    ('P003', 'Sudadera', 40.0)
]

tot = 0
for producto in productos:
    print(producto)
    tot+= producto[2]
print(f'El total es: {tot}')

#Otra forma de calcular el tot
tot=0
for i in range(len(productos)):
    producto = productos[i]
    precio = producto[2]
    tot += precio

print(f'El total es: {tot}')