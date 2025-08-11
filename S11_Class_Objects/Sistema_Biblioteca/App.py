from S11_Class_Objects.Sistema_Biblioteca.Bilblioteca import Biblioteca
from S11_Class_Objects.Sistema_Biblioteca.Libro import Libro

Libro1 = Libro(titulo="1000 anios de Soledad", autor="Garcia Marquez", genero="Romance")
Libro2 = Libro(titulo="1000 anios de Soledad", autor="Garcia Marquez", genero="Romance")
Libro3 = Libro(titulo="1000 anios de Soledad", autor="Garcia Marquez", genero="Romance")


Biblioteca1 = Biblioteca(nombre="Municipal de la La Paz")
Biblioteca1.agregar_libro(Libro1)
Biblioteca1.agregar_libro(Libro2)
Biblioteca1.agregar_libro(Libro3)
Biblioteca1.buscar_libro_autor("garcia marquez")


# Libro1.mostrar_libro()