#Ver la lomgitud de una cadena con len()

cadena1 = 'Como estas???, todo bien...que tal novia'
print(f'La cadena tiene {len(cadena1)} caracteres, incluyendo espacios.')

contador = 0
for i in cadena1:
    contador+=1

print(contador)    