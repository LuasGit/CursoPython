rango = int(input('Ingrese un rango: ').strip())
sum = 0
i = 1
while i<=rango:
    sum+=i
    i+=1
print(f'El total de la sumatoria hasta {rango} es: {sum}')