class ManejoArchivos:

    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self): # Se llama de manera automatica
        print('Entrando al recurso.'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print("Cerrando el recurso".center(50,'-'))
        if self.nombre: # Si esta apuntando a un objeto
            self.nombre.close()#Cerramos


        #       Desarrolo web backend
        # Contenido
        # 1.Principal de la comunicacion cliente servidor
        # 2.Desarrollo de la logica de negocios
        # 3.Persistencia de datos
        # 4.Desarrolo de aplicaciones web con arquitectura mvc
        # 5.Desarolo basada en aplicaciones Web con Framework. )
        # 6. Arquitectura basada en servidores

