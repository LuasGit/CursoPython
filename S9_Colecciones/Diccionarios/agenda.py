agenda = {
    'Alberth':{
        'telefono':73017265,
        'email':'alberth@gmail.com',
        'direccion':'C/batalla de Iruya'
    },
    'Luis':{
        'telefono':78778900,
        'email':'Luisinho@gmail.com',
        'direccion':'C/batalla de Ingavi'
    }    
}

for key, value in agenda.items():
    print(f'{key} y sus datos son: {value}')
#Accediendo a un contacto en especfico
print(f'''Informacion del contacto de Alberth
      Telefono: {agenda["Alberth"]["telefono"]}
      Email: {agenda["Alberth"]["email"]}
      Direccion: {agenda.get("Alberth").get("direccion")}''')#accediendo primero al key "Alberth", luego a su valor, dentro solicitamos la key de telefono, y nos desplegara su valor

#Borrando a luisinho
del agenda['Luis']

# o agenda.pop('Luis')
print(agenda)

#Agregando a Andrea
agenda["Andrea"] = {
    'telefono':34223344,
    'email': 'Andrea@gmail.com',
    'direccion':'Plaza Murillo'
}

print(agenda)