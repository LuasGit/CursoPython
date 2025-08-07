#**kwargs - keyword arguments (key, value) como un diccionario
def superheroe_poderes(name, *args, **kwargs):
    print(f'El nombre es: {name}')
    for poder in args:
        print(f'Poder: {poder}')
    for key,val in kwargs.items():
        print(f'{key}:{val}')


superheroe_poderes("Spiderman", "Sentido Aracnido", "Superpower", edad=20, compania = 'marvel')

def sumatoria_cuadrados(*args):
    cuadrados = [x ** 2 for x in args]
    print(sum(cuadrados))


sumatoria_cuadrados(1,2,3,4,5,6,7,8)