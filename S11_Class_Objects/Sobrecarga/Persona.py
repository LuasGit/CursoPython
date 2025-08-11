class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otra_persona):
        return (self.nombre + otra_persona.nombre)

    def __sub__(self, otra_persona):
        return (self.edad - otra_persona.edad)
if __name__ == '__main__':
    persona1 = Persona('Alberth', 23)
    persona2 = Persona('Jose', 45)
    print(persona1 + persona2)
    print(persona1 - persona2)