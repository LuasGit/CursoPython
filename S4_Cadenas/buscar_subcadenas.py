#Buscaremos subcadenas
cadena = 'Hallo, world'
es_mundo_indice = cadena.find('world') 
print(es_mundo_indice)

es_hola_indice = cadena.find('hallo')
print(es_hola_indice) #Imprimira -1, ya que no es lo mismo 'hallo' que 'Hallo'
 

