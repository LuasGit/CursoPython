lista_canciones = [] 
num = int(input('Introduzca cuantas canciones queire agregar: ').strip())
for i in range (num):
    musica = input('Introduzca el nombre de la musica: ').strip()
    lista_canciones.append(musica)
{lista_canciones.sort()}
print(f'la lista de manera ordenada ASC: {lista_canciones}')
{lista_canciones.sort(reverse=True)}
print(f'la lista de manera ordenada DESC: {lista_canciones} ')