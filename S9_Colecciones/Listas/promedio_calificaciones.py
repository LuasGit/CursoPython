num_calificiones = int(input('Introduzca el numero de calificaciones: ').strip())
lis_calificacion = []
for calificacion in range(num_calificiones):
    nota = float(input(f'Ingrese la nota para la calificacion {calificacion+1}: ').strip())
    lis_calificacion.append(nota)

tot=0
for calificacion in lis_calificacion:
    tot+= calificacion
    
#O tambien puedes usar sum(iterable)
suma_total = sum(lis_calificacion)
print(f'Tu promedio de calificacion de {lis_calificacion} es: {tot/len(lis_calificacion)}')
print(f'Tu promedio de calificacion de {lis_calificacion} es: {suma_total/len(lis_calificacion)}')
