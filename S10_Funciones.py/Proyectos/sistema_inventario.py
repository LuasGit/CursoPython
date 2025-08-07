#Crearemos un sistema de inventario, este tendra a su vez un menu por consola. Todo esto por funciones
def agregar():
    global lista_productos
    #Primero verificaremos el id introducido
    producto = {} #Creamos un diccionario vacio
    producto['Id'] = input('Id: ').strip() #Pedimos el id

    if not verificar(producto.get('Id')):
        producto['Nombre'] = input('Nombre Producto: ').strip()
        producto['Precio'] = float(input('Precio: ').strip())
        producto['Cantidad'] = int(input('Cantidad: ').strip())
        lista_productos.append(producto)
        print('Su producto fue aniadido con exito.')
    else:
        print(f'Ese producto con el ID {producto["Id"]} ya se encuentra en el inventario.')    

def eliminar():
    global lista_productos
    #Primero verificaremos el id introducido
    producto = {} #Creamos un diccionario vacio
    producto['Id'] = input('Id: ').strip() #Pedimos el id
    if verificar(producto['Id']):
        for element in lista_productos:
            if element.get('Id') == producto['Id']:
                lista_productos.remove(element)
                print('Su producto fue eliminado.')
                break
    else:
        print('El producto no existe')

def mostrar():
    global lista_productos
    print('Lista de Productos:')
    for producto in lista_productos:
        print(f'Id: {producto["Id"]}')
        print(f'Nombre: {producto["Nombre"]}')
        print(f'Precio: {producto["Precio"]}')
        print(f'Cantidad: {producto["Cantidad"]}')
        
        
def verificar(id):
    global lista_productos
    is_product = False #Primero, asumimos que no esta en el inventario
    for elemento in lista_productos:
        if elemento.get('Id') == id:
            is_product = True
            break
    return is_product

def buscar_id(id):
    global lista_productos
    for i in lista_productos:
        if not i.get('Id') == id:
            continue
        print(f"El producto es el siguiente")
        print(f'Id: {i["Id"]}')
        print(f'Nombre: {i["Nombre"]}')
        print(f'Precio: {i["Precio"]}')
        print(f'Cantidad: {i["Cantidad"]}')
        break
    
def menu():
    salir = False
    while not salir:
        option = int(input('''Bienvenido al Inventario de Productos.
                        Digite una opcion:
                        1. Agregar Producto
                        2. Eliminar Producto
                        3. Mostrar Productos
                        4. Buscar por Id 
                        5. Salir\n\tDigite la opcion: ''').strip())
                        
        if option == 1:
            agregar()
        elif option == 2:
            eliminar()
        elif option == 3:
            mostrar()
        elif option == 4:
            buscar_id()
        elif option == 5:
            print('Saliendo')
            salir = True
        else:
            print('Digite las opciones permitidas.')
            
         
lista_productos = []

if __name__ == '__main__':
    menu()