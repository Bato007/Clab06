import hashlib, string, random
from base64 import b64encode

txtname = 'lab6.txt'
def login(username, password):
    return True

def register(username, password):
    salt = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=13))
    # Se crea el has
    hash = hashlib.sha256()
    hash.update(bytes(password, 'utf-8'))
    hash.update(bytes(salt, 'utf-8'))
    temp = hash.digest()
    hashed = b64encode(temp).decode('utf-8')

    # Se escriben en el txt
    line = ' '.join([username, salt, hashed])
    file = open(txtname, 'a')
    file.write(line)
    file.close()

option = '0'
print('\tBienvenido')
while (option != '3'):
    # Se muestra el menu
    print('\n\tMenu')
    print('1. Login')
    print('2. Registrarse')
    print('3. Salir')
    option = input('Ingrese la opcion que desea: ')

    # Se decide que hacer
    if option == '1':
        print('\n\tLogin')
        username = input('Ingrese su usuario: ')
        password = input('Ingrese su contraseña: ')
        logged = login(username, password)
        if (logged):
            print('Ha iniciado sesion con exito')
        else:
            print('El usuario o la contraseña es incorrecta')
    elif option == '2':
        print('\n\tRegistrarse')
        username = input('Ingrese su usuario: ')
        password = input('Ingrese su contraseña: ')
        register(username, password)
        print('Se ha registrado con exito')
    elif option == '3':
        print('Gracias por utilizar el sistema')
    else:
        print('Opcion invalida')

