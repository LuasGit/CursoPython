#Verificaremos si hay esta en un rango
VALOR_MIN = 0
VALOR_MAX = 5
valor1, valor2 = map(int, input("Ingrese dos numeros: ").split())
is_inside1 = VALOR_MIN <= valor1 <= VALOR_MAX
is_inside2 = VALOR_MIN <= valor2 <= VALOR_MAX

print(is_inside1, is_inside2)
