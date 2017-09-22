def rc4(key, inputStream):
    ''' returns the RC4 encoding of inputStream based on the key
    (bytes, bytes) -> bytes
    '''
    S = []
    key = bytearray(key)
    k = bytearray()
    inn = bytearray(inputStream)
    
    output = bytearray()
    
    # Key-scheduling algorithm ################################################
    
    # create a list containing ints from 0 to 255
    for i in range(0,256):
        S.append(i)
    
    j = 0
    for i in range(0,256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    
    # Pseudo-random generation algorithm ######################################
    
    i = 0
    j = 0
    
    # l doesn't get used, just needed for the loop
    for l in range(len(inn)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k.append(S[(S[i] + S[j]) % 256])
    
    # XOR the PRGA output and original input
    for i in range(len(inn)):
        output.append(k[i] ^ inn[i])

    return output
    
    
    
    