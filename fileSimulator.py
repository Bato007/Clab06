from hashlibExamples import sha256Res, sha512Res, blake2bRes
import hmac, hashlib, base64

hashes = ['sha256','sha512','blake2b']


"""
Convierte un archivo en hash al brindar una llave y modo
"""
def enc(file, key, hashMode):
    encFile =  open(file, 'r')
    chain = encFile.read().encode('utf-8')

    if hashMode == 'sha256':
        string = sha256Res(chain,key)
    elif hashMode == 'sha512':
        string = sha512Res(chain,key)
    elif hashMode == 'blake2b':
        string = blake2bRes(chain,key)
    else:
        return '\n--------\nBAD ENTRY!\n-------\n'

    return string

"""
Identifica si el mensaje hash es correspondiente con la llave y el archivo brindado
"""
def dec(file, key, hashMsg, hashMode):
    for i in range(len(hashes)):
        if hashMode == hashes[i]:
            resultHash = enc(file, key, hashMode)[0] #Se compara unicamente bin
    if resultHash == hashMsg[0]:
        return True

    return False
    
"""
Compara los archivos apenas modificados utilizando la misma llave
"""
def compareHash(route1, route2, hashMode, key):
    result = '\nHASH MODE --> '+str(hashMode)+'\n----------------------------------\n'
    string_1 = ''
    string_2 = ''
    file_1 =  open(route1, 'r')
    file_2 =  open(route2, 'r')
    chain_1 = file_1.read().encode('utf-8')
    chain_2 = file_2.read().encode('utf-8')
    
    if hashMode == 'sha256':
        string_1 = sha256Res(chain_1, key)
        string_2 = sha256Res(chain_2, key)
    elif hashMode == 'sha512':
        string_1 = sha512Res(chain_1, key)
        string_2 = sha512Res(chain_2, key)
    elif hashMode == 'blake2b':
        string_1 = blake2bRes(chain_1, key)
        string_2 = blake2bRes(chain_2, key)
    else:
        return '\n--------\nBAD ENTRY!\n-------\n'

    mode = ['Binary', 'Hex', 'Base64']
    for i in range(3):
        if string_1[i] != string_2[i]:
            result += str(mode[i])+': OK! Ambas cadenas HASH son diferentes\n'
        else:
            result += str(mode[i])+': WARNING! Las cadenas son identicas\n'

    return [result, string_1, string_2]

route = 'fileSim/test1.txt'
route2 = 'fileSim/test2.txt'
key = 'justakeyLoL1'
mode = 'blake2b'
msg = enc(route, key, mode)
msg2 = enc(route2, key, mode)

print('HASH -->',msg)
print(compareHash(route, route2, mode, key)[0])
print('EJEMPLO 1\nCorresponde el hash1 con el achivo1 y la llave?',dec(route, key, msg, mode))
print('\nEJEMPLO 2\nCorresponde el hash2 con el achivo1 y la llave?',dec(route, key, msg2, mode))