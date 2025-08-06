monto = float(input('Ingrese el total: '))
miembro = input('Es ud miembro(si/no): ').strip().lower()

if monto > 1000 and miembro == 'si':
    monto -= (monto * 0.10)
elif miembro == 'si':
    monto -= (monto *0.05)    
elif monto > 1000 :
    monto-= (monto * 0.03)
else:
    monto -= 0
print(f'El total a pagar es: {monto:.2f}')