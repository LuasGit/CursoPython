def factorial_normal(numero):
    if numero == 0:
        print(1)
    for i in range(1, numero):
        numero *= i
    print(numero)
factorial_normal(6)


def factorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * (factorial_recursivo(numero-1))

print(factorial_recursivo(10))