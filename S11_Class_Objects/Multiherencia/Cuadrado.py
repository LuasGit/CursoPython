from S11_Class_Objects.Multiherencia.Color import Color
from S11_Class_Objects.Multiherencia.FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho