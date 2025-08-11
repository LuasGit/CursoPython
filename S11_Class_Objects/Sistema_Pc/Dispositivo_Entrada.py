class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return f'Marca: {self._marca}, Tipo: {self._tipo_entrada}'

class Raton(DispositivoEntrada):
    cont_ratones = 0
    def __init__(self, marca, tipo_entrada):
        Raton.cont_ratones += 1
        self._id_raton = self.cont_ratones
        super().__init__(marca, tipo_entrada)

    @property
    def id_raton(self):
        return self._id_raton
    @id_raton.setter
    def id_raton(self, id_raton):
        self._id_raton = id_raton

    @classmethod
    def contar_ratones(cls):
        return cls.cont_ratones

    def __str__(self):
        return f'Raton: {self._id_raton}, {super().__str__()}'

class Tecla(DispositivoEntrada):
    cont_teclados = 0
    def __init__(self, marca, tipo_entrada):
        Tecla.cont_teclados += 1
        self._id_tecla = self.cont_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Tecla: {self._id_tecla}, {super().__str__()}'

    @property
    def id_tecla(self):
        return self._id_tecla
    @id_tecla.setter
    def id_tecla(self, id_tecla):
        self._id_tecla = id_tecla

    @classmethod
    def cont_teclados(cls):
        return cls.cont_teclados


if __name__ == '__main__':
    raton1 = Raton('marca', 'tipo de raton')
    raton2 = Raton('marca', 'tipo de raton')
    print(raton1)
    print(raton2)
    print(Raton.cont_ratones)
    print(raton1.mro())