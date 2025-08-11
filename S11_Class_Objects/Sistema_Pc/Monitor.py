class Monitor:
    cont_monitor = 0
    def __init__(self, marca, tamanio):
        Monitor.cont_monitor += 1
        self._id = Monitor.cont_monitor
        self._marca = marca
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    @classmethod
    def cont_teclads(cls):
        return cls.cont_monitor

    def __str__(self):
        return f'Id: {self._id}, Marca: {self._marca}, Tamanio: {self._tamanio}'