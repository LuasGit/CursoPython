class Aritmetica:
    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2
    
    def sumar(self):
        print(self.operador1 + self.operador2)
    
    def restar(self):
        print(self.operador1 - self.operador2)

    def multiplicar(self):
        print(self.operador1 * self.operador2)
    
    def dividir(self):
        print(self.operador1 / self.operador2)

if __name__ == "__main__":
    a = Aritmetica(23 , 43)
    b = Aritmetica(123 , 54)
    
    a.sumar()
    a.restar()
    a.dividir()
    b.restar()
    b.multiplicar()