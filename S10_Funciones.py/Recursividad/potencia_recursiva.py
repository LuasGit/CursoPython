#potencai recursiva, pediremos 2 parametros a, que es el numero, Y B QUE ES LA exponenteCION

def potenciacion_recursiva(num, exponente):
    if exponente == 0:
        return 1
    else:
        return num * (potenciacion_recursiva(num, exponente-1))
    
print(potenciacion_recursiva(6,3))