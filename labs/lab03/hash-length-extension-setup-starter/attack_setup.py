from md5p import *

KEY = "secret"

#############
### Alice ###
#############

def createToken(message):
    return md5(KEY + message).hexdigest()

###########
### bob ###
###########

def verifyToken(message, token):

    return (token == md5(KEY + message).hexdigest())

###############
### Mallory ###
###############


def forgeIllegalPayload(message, token, extension):
    '''
    In this function, you are not allowed to:
    - call the function createToken
    - use the secret key
    However, you might know the length of the secret key (6)
    '''
    # set MD5 to contain state of token. This will 'restore' the md5 to state
    # it would have been in if it recieved a string in the format secret + m + 
    # [padding req'd for m and secret].
    
    h = md5(state=token.decode("hex"),count=512)
    
    # add extension to it
    h.update(extension)
    
    # this should be the output the server gets for the token
    illegalToken = h.hexdigest()
    
    # since the server will prepend the secret to a message when checking it,
    # we simply need to send it a message of m + [padding req'd for m and secret] + extension. 
    illegalMessage = message + padding(8 * (len(message) + len(KEY)))  + extension
    
    return illegalToken, illegalMessage
    

#############
### main ####
#############

if __name__ == "__main__":
    
    ##################################
    ################################
    # exchange between Alice and Bob
    ################################
    
    message = "get balance"
    # alice creates a message and its corresponding token and send them to Bob
    token = createToken(message)
     # Bobs receives the token and verifies it
    # prints true since the token is legitimate
    print(verifyToken(message, token))
    print(token)

    ##################################
    # exchange between Mallory and Bob
    ##################################
    
    extension = " after withdrawing 100"
     # Mallory forges an illegal token for the message + extension and send them to Bob
    illegalToken, IllegalMessage = forgeIllegalPayload(message, token, extension)
    # Bobs receives the token and verifies it
    # prints true, if the illegalToken is valid
    print(verifyToken(IllegalMessage, illegalToken))

