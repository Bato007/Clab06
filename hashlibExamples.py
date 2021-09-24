import hashlib
import codecs
import hmac

# CIFRADO sha256
def sha256Res(cadena, key=None):
    resHex = ''
    if key != None:
        resHex = hmac.new(key.encode('utf-8'), msg=cadena, digestmod=hashlib.sha256).hexdigest()
    else:
        m = hashlib.sha256()
        m.update(cadena)
        resHex = m.hexdigest()

    resBin = bin(int(resHex, 16))[2:].zfill(8)
    res64 = codecs.encode(codecs.decode(resHex, 'hex'), 'base64').decode()

    return [resBin, resHex, res64, cadena]


# CIFRADO sha512
def sha512Res(cadena, key=None):
    resHex = ''
    if key != None:
        resHex = hmac.new(key.encode('utf-8'), msg=cadena, digestmod=hashlib.sha512).hexdigest()
    else:
        m = hashlib.sha512()
        m.update(cadena)
        resHex = m.hexdigest()
    
    resBin = bin(int(resHex, 16))[2:].zfill(8)
    res64 = codecs.encode(codecs.decode(resHex, 'hex'), 'base64').decode()

    return [resBin, resHex, res64, cadena]


# CIFRADO blake2b
def blake2bRes(cadena, digestSize=64, key=None):
    resHex = ''
    if key != None:
        resHex = hmac.new(key.encode('utf-8'), msg=cadena, digestmod=hashlib.blake2b).hexdigest()
    else:
        m = hashlib.blake2b()
        m.update(cadena)
        resHex = m.hexdigest()

    resBin = bin(int(resHex, 16))[2:].zfill(8)
    res64 = codecs.encode(codecs.decode(resHex, 'hex'), 'base64').decode()

    return [resBin, resHex, res64, cadena]   


# Mostrar resultado
def printRes(nombre, res):
    print('-'*100)
    print('RESULTADO DE', nombre)
    print('CADENA PROBADA', res[3])
    print('-'*100)
    print('\nBinario', res[0])
    print('\nHex', res[1])
    print('\nbase64', res[2])
    print('-'*100)
    return ''

"""
print(printRes('sha256', sha256Res(b'quiero ir a dormir')))
print(printRes('sha512', sha512Res(b'quiero ir a dormir')))
print(printRes('blake2b', blake2bRes(b'quiero ir a dormir', 64)))
"""