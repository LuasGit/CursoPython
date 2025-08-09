class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca #Atributo publico
        self._modelo = modelo #Atributo Protegido
        self._color = color
    
    def conducir(self):
        print(f'''Conduciendo el coche:
        marca: {self._marca}
        modelo: {self._modelo}
        color: {self._color}''')

    #GETTERS AND SETTERS
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    # def get_color(self):
    #     return self._color

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._marca = color


if __name__ == '__main__':
    coche1 = Coche('toyota','yaris','azul')
    coche1.marca = 'dasda'
    coche1.conducir()
    setattr(coche1, 'auto', 'dadad') #Se puede agregar un atributo ajeno a la clase, solo a un objeto
    coche1.conducir()
    print(f'Atriutos del coche: {coche1.__dict__}')
