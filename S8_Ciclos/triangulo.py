num_row = int(input('Introduzca el numero de filas: ').strip())
for i in range(1,num_row + 1):
    blank_spaces = ' '*(num_row-i)
    print(blank_spaces+ ('*' * (2*i-1)))