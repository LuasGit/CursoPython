class Aritmetica:
    #Python solo toma el ultimo metodo
    # def __init__(self, _operador1):
    #     self._operador1 = _operador1

    def __init__(self, _operador1= None, _operador2 = None):
        self._operador1 = _operador1
        self._operador2 = _operador2
    
    def sumar(self):
        print(self._operador1 + self._operador2)
    
    def restar(self):
        print(self._operador1 - self._operador2)

    def multiplicar(self):
        print(self._operador1 * self._operador2)
    
    def dividir(self):
        print(self._operador1 / self._operador2)

    @property
    def operador1(self):
        return self._operador1
    @property
    def operador2(self):
        return self._operador2
    @operador1.setter
    def operador1(self, value):
        self._operador1 = value
    @operador2.setter
    def operador2(self, value):
        self._operador2 = value


if __name__ == "__main__":
    a = Aritmetica(23 , 43)
    b = Aritmetica(123 , 54)
    
    a.sumar()
    a.restar()
    a.dividir()
    b.restar()
    b.multiplicar()
    
