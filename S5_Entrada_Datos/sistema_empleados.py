nombre_empleado = input('Introduzca el nombre del empleado: ')
edad_empleado = int(input('Introduzca la edad del empleado: '))
salario = float(input('Introduzxa el salario del empleado: '))
es_jefe_dep = input('Es jefe departamento (Si/No): ')


es_jefe_dep = es_jefe_dep.lower() == 'si'
print(es_jefe_dep)