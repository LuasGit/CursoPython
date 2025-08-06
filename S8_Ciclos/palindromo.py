cadena = input('Introduzca una cadena para verificar si es palindroma: ').strip().lower()
original = cadena
reverse = ''
for letra in cadena:
    reverse = letra + reverse 
print(reverse)

#Segunda forma
# for letra in range (len(cadena)-1, -1, -1):
#     reverse += cadena[letra]

print('Es palindroma' if original == reverse else "No es palindroma")