#Definimos una clase
class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')

#Instanciando uan clase

if __name__ == '__main__':
    persona1 = Persona('Alan','Martinez') 
    persona1.mostrar()
    
    persona2 = Persona(nombre="Jorge",apellido='Martinez')
    persona2.mostrar()