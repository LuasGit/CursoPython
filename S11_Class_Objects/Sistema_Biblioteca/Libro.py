class Libro:
    def __init__(self, autor, titulo, genero):
        self._autor = autor
        self._titulo = titulo
        self._genero = genero

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    def mostrar_libro(self):
        print(f'Nombre: {self._autor}, titulo: {self._titulo}, genero: {self._genero}')