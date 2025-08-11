from S11_Class_Objects.Multiherencia.Cuadrado import Cuadrado
from S11_Class_Objects.Multiherencia.FiguraGeometrica import FiguraGeometrica

print('Creacion Objeto Cuadrado'.center(50,'-'))
# figura = FiguraGeometrica() , No se puede instanciar una clase abstracta
cuadrado1 = Cuadrado(lado=-8, color="Rojo")
print(f'El area del cuadrado es: {cuadrado1.calcular_area()}')
#MRO - Method Resolution Order
print(Cuadrado.mro())