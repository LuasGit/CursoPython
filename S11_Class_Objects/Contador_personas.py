class Persona:
    contador_de_personas = 0
    def __init__(self, nombre, apellido):
        Persona.contador_de_personas += 1
        self.id = Persona.contador_de_personas #Cada vez que se instancie un objeto, el contador aumenta.
        self.nombre = nombre
        self.apellido = apellido
    def mostrar_persona(self):
        print(f'''
        id: {self.id}
        nombre: {self.nombre}
        apellido: {self.apellido}''')

    @staticmethod
    def  get_contador_de_personas_estatico():
        print(f'''Metodo estatico''')
        return Persona.contador_de_personas
    @classmethod
    def get_contador_de_personas_clase(cls):
        print(f'''Metodo estatico''')
        return cls.contador_de_personas #Metodo de CLASE

#Main
if __name__ == '__main__':
    persona1 = Persona('Alberth Saul', 'Mamani Pita')
    persona1.mostrar_persona()

    print(f'Contador de personas (clase):{Persona.get_contador_de_personas_clase()}')