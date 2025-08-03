#Este sera un generador de email a partir de cadenas dadas

nombre = 'Alberth Mamani Pita'
empresa = 'Monster Inc'
dominio = 'com.minc'

nombre_dividido = nombre.split()
empresa_dividida = empresa.split()

primera_parte = ''.join([nombre_dividido[0].lower()+'.'+nombre_dividido[1].lower()+'.'+nombre_dividido[2].lower()])
segunda_parte = ''.join(['@'+empresa_dividida[0].lower()+empresa_dividida[1].lower()+'.'+dominio])
email = primera_parte + segunda_parte
print(email)
print(f'otra forma: {primera_parte}{segunda_parte}')


#EJERCICIOS PARA PRACTICAR
new_word = ''
for i in range (len(nombre)-1,-1,-1):
    new_word += nombre[i]
    
print(new_word)

original = input(str('Introduce una palabra: '))
reverse = ''
for i in range(len(original)-1, -1, -1):
    reverse+=original[i]
    
if original == reverse:
    print('Es un palindromo')
else:
    print('no es palindromo' )