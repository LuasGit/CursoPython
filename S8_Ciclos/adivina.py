from random import randint
num_random = randint(1,50)
intentos = 0
num = None
while num != num_random and intentos < 20:
    num = int(input('Ingrese un numero para adivinar: ').strip())
    if num < num_random:
        print('El numero es mayor.')
    else:
        print('El numero es menor')
    intentos +=1
else:
    print('Lo adivinaste')