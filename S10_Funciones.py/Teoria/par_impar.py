#Funcion para ver si es par o no
def par_impar(*args):
    print([f"par {x}" if x % 2 == 0 else f"impar {x}" for x in args])
    

if __name__ == "__main__":
    par_impar(2, 3, 4,324,312,412,312,5,4,345)
