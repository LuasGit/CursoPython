#Verificaremos password
password = 'Alberthsaul2004'
user = 'Luas.sa'

user_verificar = input('Ingrese el nombre de usuario: ')
password_verificar = input('Ingrese la contrasenia: ')

es_correcta = user_verificar.strip() == user and password_verificar.strip() == password

print(es_correcta)