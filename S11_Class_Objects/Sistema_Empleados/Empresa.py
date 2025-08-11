from S11_Class_Objects.Sistema_Empleados.Empleado import Empleado

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_empleados_departamento(self, departamento):
        cont_empleados_dep = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                cont_empleados_dep += 1
        return cont_empleados_dep