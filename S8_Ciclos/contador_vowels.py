cadena = input('Introduzca una cadena para contar cuantas vocales tiene: ').strip().lower()
contador = 0
for letra in cadena:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador +=1
print(f'La cantidad de vocales en la cadena {cadena} son: {contador}')