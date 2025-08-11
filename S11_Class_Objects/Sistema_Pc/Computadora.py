class Computadora:
    cont_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.cont_computadoras += 1
        self._id_computadora = Computadora.cont_computadoras
        self._nombre = nombre
        self._Monitor = monitor
        self._Teclado = teclado
        self._Raton = raton

    @property
    def id_computadora(self):
        return self._id_computadora
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._Monitor
    @monitor.setter
    def monitor(self, monitor):
        self._Monitor = monitor

    @property
    def tecla(self):
        return self._Teclado
    @tecla.setter
    def tecla(self, tecla):
        self._Teclado = tecla

    @property
    def raton(self):
        return self._Raton
    @raton.setter
    def raton(self, raton):
        self._Raton = raton

    @classmethod
    def cont_computadoras(cls):
        return cls.cont_computadoras

    def __str__(self):
        return (f'Id: {self._id_computadora}, Nombre: {self._nombre}'
                f'Monitor: {self._Monitor}, Teclado: {self._Teclado}'
                f'Raton: {self._Raton}')
