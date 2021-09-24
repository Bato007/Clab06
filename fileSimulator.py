from hashlibExamples import sha256Res, sha512Res, blake2bRes

def enc(file, key):
    hash = 'Hash'
    return hash

def dec(file, key, hash):
    status = 'correct?'
    return status

def compareHash(route1, route2, hashMode):
    result = '\n'+str(hashMode)+'\n----------------------------------\n'
    string_1 = ''
    string_2 = ''
    file_1 =  open(route1, 'r')
    file_2 =  open(route2, 'r')
    chain_1 = file_1.read().encode('utf-8')
    chain_2 = file_2.read().encode('utf-8')
    
    if hashMode == 'sha256':
        string_1 = sha256Res(chain_1)
        string_2 = sha256Res(chain_2)
    elif hashMode == 'sha512':
        string_1 = sha512Res(chain_1)
        string_2 = sha512Res(chain_2)
    elif hashMode == 'blake2b':
        string_1 = blake2bRes(chain_1)
        string_2 = blake2bRes(chain_2)
    else:
        return '\n--------\nBAD ENTRY!\n-------\n'

    mode = ['Binary', 'Hex', 'Base64']
    for i in range(3):
        if string_1[i] != string_2[i]:
            result += str(mode[i])+': OK! Both keys are different\n'
        else:
            result += str(mode[i])+': WARNING! Both keys are the same\n'

    return [result,string_1, string_2]

print(compareHash('fileSim/test1.txt','fileSim/test2.txt', 'sha512')[0]) 