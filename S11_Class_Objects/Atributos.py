class Persona:
    atributo_clase = 0 #Se asocia con la clase
    def __init__(self, atributo_instancia):
        self.atributo_clase = atributo_instancia #Se asocia con el objeto a crear


#Main
if __name__ == '__main__':
    print("***Atributos de clase***")
    print(f'Atributo de clase: {Persona.atributo_clase}')
    Persona.atributo_clase = 100
    print(f'Atributo de clase: {Persona.atributo_clase}')
    persona = Persona(1)
    print(persona.atributo_clase)