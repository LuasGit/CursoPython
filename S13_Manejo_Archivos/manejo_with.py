# with open('Copia.txt', 'r') as archivo:
#     print(archivo.read())
from S13_Manejo_Archivos.manejinhos import ManejoArchivos

with ManejoArchivos('Prueba.txt') as archivinho:
    print(archivinho.read())