class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libro_autor(self, autor):
        print("Buscando libro autor", autor)
        for libro in self._libros:
            if libro.autor.strip().upper() == autor.strip().upper():
                libro.mostrar_libro()

    def buscar_libro_genero(self, genero):
        print("Buscando libro genero", genero)
        for libro in self._libros:
            if libro.genero.strip().upper() == genero.strip().upper():
                print(f'''
                titulo: {libro.titulo}, genero: {libro.genero}''')

    def mostrar_libros(self):
        for libro in self._libros:
            libro.mostrar_libro()

    def mostrar_libro(self, libro):
        libro.mostrar_libro()