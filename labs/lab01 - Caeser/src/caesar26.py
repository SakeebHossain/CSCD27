''' encrypts the plaintext with a key
    based on the caesar cipher algorithm
    and return the ciphertext
    (string, string) -> string
    REQ: key matches [0-9]*
    REQ: plaintext matches [a-z]*
'''
def encrypt(key, plaintext):
    ciphertext = plaintext # dummy instruction
    output = ""
    for letter in ciphertext:
        if letter.isalpha():
            old = ord( letter ) - 97
            new = ( old + int( key ) ) % 26 + 97
            output += chr ( new )
    return output

''' decrypts the ciphertext with a key
    based on the caesar cipher algorithm
    and returns the plaintext    return plaintext
    (string, string) -> string
    REQ: key matches [0-9]*
    REQ: ciphertext matches [a-z]*'''    
def decrypt(key, ciphertext):
    plaintext = ciphertext # dummy instruction
    output = ""
    for letter in ciphertext:
        if letter.isalpha():
            old = ord( letter ) - 97
            new = ( old - int( key ) ) % 26 + 97
            output += chr ( new )
    return output
