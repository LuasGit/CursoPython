numeros = [1,2,3,4,5,6]
cubos = [x**3 for x in numeros]
print(cubos)

numeros = range(15+1)
print(numeros) #No es una lista, es un rango    
pares = [x for x in numeros if x % 2 == 0]
print(pares)

#Saludando
nombres = ['alberth','ana','octavia']
print([f'Hola {saludo}' for saludo in nombres])