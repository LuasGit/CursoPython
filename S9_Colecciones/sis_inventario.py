num = int(input('Introduzca el numero de productos para aniadir: ').strip())
products = []
for i in range (num):
    elemento = {}
    print('Introduzca datos del producto:',i+1)
    elemento["Id"] = input('Introduzca un id: ').strip()
    elemento["nombre_producto"] = input('Introduzca el nombre del producto: ').strip()
    elemento["precio"] = float(input('Introduzca el precio del producto: ').strip())
    elemento["cantidad"] = int(input('Introduzca la cantidad del producto: ').strip())
    products.append(elemento)

for i, producto in enumerate(products):
    print(f'{i+1} - {producto}')

#Buscar por id
id_buscar = input('Id a buscar: ').strip()
producto_encontrado = None
for producto in products:
    if producto.get("Id") == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(producto_encontrado)
else: 
    print('El producto no fue encontrado')