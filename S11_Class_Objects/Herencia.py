class Animal:#Clase Padres o Superclase
    def comer(self):
        print("Como muchas veces al dia.")
    def dormir(self):
        print("Duermo muchas horas.")

class Perro(Animal): #Entre parentesis la superclase, o clase de la cual heredara
    def hacer_sonido(self):#Metodo independiente, solo la clase Perro o subclases podran tener este metodo.
        # Aunque hereda all de su superclase
        print("Puedo ladrar.")

    #Sobreescribimos el metodo padre para adaptarlo a la clase hija
    def comer(self):
        print("Como muchos huesos, soy un perro")

#Main
if __name__ == "__main__":
    Animal1 = Animal()
    Animal1.comer()
    perro1 = Perro()
    perro1.dormir()
    perro1.hacer_sonido()
    perro1.comer()