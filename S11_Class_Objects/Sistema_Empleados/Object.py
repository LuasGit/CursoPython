class Persona: #TODOS LOS OBJETOS DERIVAN DE LA CLASE PADRE (OBJECT)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #Sobreescribimos, siempre manda una cadena
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Direccion: {super.__str__(self)}' #Con super. accedemos a la clase padre


if __name__ == '__main__':
    persona1 = Persona('Alberth', 22)
    print(persona1) #El metodo dunder __str__ se manda automaticamente
