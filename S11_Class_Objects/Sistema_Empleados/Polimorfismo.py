class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Ladrando...")

class Gato(Animal):
    def hacer_sonido(self):
        print("Maullando...")

#funcion polimorfica
def hacer_sonido_animal(Animal):#DuckTyping
    Animal.hacer_sonido() #Python mostrara segun lo enviado. Esto por su dinamismo.

#MAIN
if __name__ == '__main__':
    #Polimorfismo
    print('Clase Padre')
    Animal1 = Animal()
    Animal1.hacer_sonido()
    print('Clase Gato')
    Gato1 = Gato()
    Gato1.hacer_sonido()
    print('Clase Perro')
    Perro1 = Perro()
    #Perro1.hacer_sonido()


    print('FUNCION POLIMORFICA')
    hacer_sonido_animal(Perro1)
