from S11_Class_Objects.Sistema_Empleados.Empleado import Empleado
from S11_Class_Objects.Sistema_Empleados.Empresa import Empresa

print('Sistema de Empleados:')

#Instanciamos una empresa
empresa1 = Empresa(nombre='Macunga')
empresa1.contratar_empleado("Juanito",1)
empresa1.contratar_empleado("Elias",2)
empresa1.contratar_empleado("Facundo",1)
empresa1.contratar_empleado("Mordecai",2)
empresa1.contratar_empleado("Rambo",1)
empresa1.contratar_empleado("Miguel",2)
empresa1.contratar_empleado("Jorge",1)

print(f'Total de empleados: {Empleado.obtener_total_empleados()}')
print(f'Total de empledos del departamento 1: {empresa1.obtener_empleados_departamento(1)}')