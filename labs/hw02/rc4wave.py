from Crypto.Cipher import ARC4
import wave

def encrypt(key_filename, input_filename, output_filename):
    ''' 
    Encrypts the wave input file (input_filename) with the key (key_filename) using the rc4 cipher (from pycrypto)
    and writes the wave output file (output_filename). 
    The wave output file must be a playable wave file.
    (string, string, string) -> None
    '''
    # get key from inside key file
    key = open(key_filename, "rb").read()
    
    # initialize RC4
    cipher = ARC4.new(key)
    
    # prepare output file
    output = wave.open(output_filename, "wb")    
    
    # open wav file
    wav = wave.open(input_filename, "rb")
    
    # get params
    params = wav.getparams()
    
    # set original params back in output file
    output.setparams(params)        
    
    # read frames into file
    plaintext = wav.readframes(wav.getnframes())
    
    # encrypt ciphertext
    ciphertext = cipher.encrypt(plaintext)
    
    # write ciphertext in an output file
    output.writeframes(ciphertext)
    
    return ciphertext
    
def decrypt(key_filename, input_filename, output_filename):
    ''' 
    Decrypts the wave input file (input_filename) with the key (key_filename) using the rc4 cipher (from pycrypto)
    and writes the wave output file (output_filename). 
    The wave output file must be a playable wave file. 
    (string, string, string) -> None
    '''
    # get key from inside key file
    key = open(key_filename, "rb").read()
    
    # initialize RC4
    cipher = ARC4.new(key)
    
    # prepare output file
    output = wave.open(output_filename, "wb")    
    
    # open wav file
    wav = wave.open(input_filename, "rb")
    
    # get params
    params = wav.getparams()
    
    # set original params back in output file
    output.setparams(params)        
    
    # read frames into file
    plaintext = wav.readframes(wav.getnframes())
    
    # encrypt ciphertext
    ciphertext = cipher.decrypt(plaintext)
    
    # write ciphertext in an output file
    output.writeframes(ciphertext)
    
    return ciphertext
