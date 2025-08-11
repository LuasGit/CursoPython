#ABC = Abstract Base Class
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho): #Usando la validacion
            self._ancho = ancho
        else:
            self._ancho = 0
            print('Valor erroneo de ancho')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('Valor erroneo de alto')
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho): #Validando en el set
        if self._validar_valores(ancho):
            self._ancho = ancho
    def _validar_valores(self, valor): #Metodo encapsulado, solo en la clase
        return True if 0 < valor < 10 else False

    #Metodo abstracto, obligamos a las clase hijas a implementarla. Las clases abstractas NO PUEDEN SER INSTANCIADAS
    @abstractmethod
    def calcular_area(self):
        pass
