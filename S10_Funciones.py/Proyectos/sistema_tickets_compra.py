snacks = [
    {"id": 1, "nombre": "Papas fritas", "precio": 5.0},
    {"id": 2, "nombre": "Chocolatina", "precio": 4.5},
    {"id": 3, "nombre": "Galletas", "precio": 3.5},
    {"id": 4, "nombre": "Chicle", "precio": 1.0},
    {"id": 5, "nombre": "Maní salado", "precio": 2.5},
    {"id": 6, "nombre": "Barra energética", "precio": 6.0},
    {"id": 7, "nombre": "Pan con queso", "precio": 3.0},
    {"id": 8, "nombre": "Pastelito", "precio": 4.0},
    {"id": 9, "nombre": "Yogur", "precio": 3.5},
    {"id": 10, "nombre": "Refresco", "precio": 5.0}
]
factura = []


#Funciones

def mostrar_snacks():
    global snacks
    if snacks:
        print('----- Lista de Snacks -----')
        for snack in snacks:
            print(f'''
{"Id:".ljust(10)}{str(snack.get("id", "")).ljust(10)}
{"Nombre:".ljust(10)}{snack.get("nombre", "").ljust(20)}
{"Precio:".ljust(10)}{str(snack.get("precio", "")).ljust(10)} Bs''')
    else:
        print('No hay productos.')

def comprar_snack():
    global snacks
    global factura
    id_snack = int(input('\nPor favor ingrese el (id) del snack: ').strip())
    for snack in snacks:
        if snack.get('id') == id_snack:
            factura.append(snack)
            print("Agregado.")

def mostrar_factura():
    global factura
    for elemento in factura:
        print(f'''
{"Id:".ljust(10)}{str(elemento.get("id","")).ljust(10)}
{"Nombre:".ljust(10)}{elemento.get("nombre", "").ljust(20)}
{"Precio:".ljust(10)}{str(elemento.get("precio", "")).ljust(10)} Bs''')
    tot = 0
    for i in factura:
        tot+=i.get("precio")
    print(f'\nTotal es: {tot} Bs')
    

def menu():
    salir = False
    while not salir:
        print("***Welcum, seleccione una opcion***")
        print(f'''
              1. Mostrar Productos
              2. Comprar Producto
              3. Mostrar Factura
              4. Salir''')
        option = int(input('Seleccione una opcion: ').strip())
        if option == 1:
            mostrar_snacks()
        elif option == 2:
            comprar_snack()
        elif option == 3:
            mostrar_factura()
        elif option == 4:
            salir = True
        else:
            print('por favor,no sea pndj. Digite una de las opciones')

if __name__ == "__main__":
    menu()