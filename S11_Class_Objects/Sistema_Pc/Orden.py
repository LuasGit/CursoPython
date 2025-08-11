class Orden:
    cont_orden = 0
    computadoras = []
    def __init__(self):
        Orden.cont_orden += 1
        self._id_orden = Orden.cont_orden
    @property
    def id_orden(self):
        return self._id_orden

    @classmethod
    def cont_orden(cls):
        return cls.cont_orden

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        return (f'Orden: {self.id_orden}: '
                f'{self.mostrar_computadoras()}')

    def mostrar_computadoras(self):
        for computadora in self.computadoras:
            print(computadora)

if __name__ == '__main__':
    print(Orden.cont_orden)
