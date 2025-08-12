from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPelicula
if __name__ == '__main__':
    salir  = False
    while not salir:
        try:
            print('Por favor, ingrese una de las siguientes opciones:\n'
                  '1. Agregar Pelicula\n'
                  '2. Listar Peliculas\n'
                  '3. Eliminar Peliculas\n'
                  '4. Salir\n')
            option = int(input())
            if option == 1:
                name = input('Por favor, ingrese el nombre de la Pelicula: ').strip()
                pelicula = Pelicula(name)
                CatalogoPelicula().agregar_pelicula(pelicula)
            elif option == 2:
                CatalogoPelicula().listar_peliculas()
            elif option == 3:
                CatalogoPelicula().eliminar_peliculas()
            elif option == 4:
                salir = True
            else:
                print('Opcion no valida')
        except Exception as e: print(f'Ocurrio un error: {e}, {type(e)}')
