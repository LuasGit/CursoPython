import os #importando el paquete de os
class CatalogoPelicula:
    path_file = "Peliculas.txt"

    @property
    def path(self):
        return self._path
    @path.setter
    def nombre(self, path):
        self._path = path

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.path_file, "a", encoding='utf8') as file:
            file.write(pelicula.nombre + '\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.path_file, "r", encoding='utf8') as file:
            print("Catalogo de Peliculas".center(50, '-'))
            print(file.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.path_file)
        print(f'Eliminado {cls.path_file}')


