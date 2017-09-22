from Crypto.Cipher import XOR
import base64

''' encrypts the plaintext (utf-8) with a key
    based on the xor cipher algorithm
    and return the ciphertext (base64 encoded)
    (string, string) -> string
'''
def encrypt(key, plaintext):
    
    # Convert key and plaintext to byte format.
    b_key = key
    b_plaintext = plaintext
    
    # Initialize XOR cipher; provide the key that will be used.
    cipher = XOR.XORCipher(b_key)
    
    # Now, XOR the plaintext and inputs.
    binary_ciphertext = cipher.encrypt(b_plaintext)
    
    # Convert to Base64.
    b_ciphertext = base64.b64encode(binary_ciphertext)
    
    # Convert to ASCII (since output must be string)  
    ciphertext = str(b_ciphertext,'ascii', 'ignore')
    
    return ciphertext

''' decrypts the ciphertext (base64 encoded) with a key
    based on the xor cipher algorithm
    and returns the plaintext (utf-8)
    (string, string) -> string
'''    
def decrypt(key, ciphertext):
    
    # Decode ciphertext from base64 to bytes.
    str_ciphertext = base64.b64decode(ciphertext)

    # Convert from bytes to ASCII
    str_ciphertext = str(str_ciphertext,'ascii', 'ignore')
    
    # Convert key and plaintext to byte format.
    b_key = key
    b_ciphertext = str_ciphertext
    
    # Initialize XOR cipher; provide the key that will be used.
    cipher = XOR.XORCipher(b_key)    
    
    # Decode.
    plaintext = cipher.decrypt(b_ciphertext)
    
    return  str(plaintext,'ascii', 'ignore')
