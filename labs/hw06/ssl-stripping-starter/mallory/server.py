# https://ruslanspivak.com/lsbaws-part1/
import socket

ALICE_HOST, ALICE_PORT = '', 8080
SECLAB_HOST, SECLAB_PORT = "142.1.97.172", 80

def start_sockets():
    
    # Initialize Mallory's connection to Alice.
    alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    alice_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    alice_socket.bind((ALICE_HOST, ALICE_PORT))
    alice_socket.listen(1)    
    
    # Initialize Mallory's connection to Seclab.
    seclab_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    seclab_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    seclab_socket.connect((SECLAB_HOST, SECLAB_PORT))
    
    return alice_socket, seclab_socket


def close_sockets():
    alice_socket.close()
    seclab_socket.close()  
    
    
if __name__ == "__main__":
    
    while True:
        
        # Open socket connections between Mallory and Alice, Mallory and Seclab
        alice_socket, seclab_socket = start_sockets()
        
        # Receive POST request from Alice
        client_connection, client_address = alice_socket.accept()
        request = client_connection.recv(1024)
        
        # Send POST request to server
        seclab_socket.sendall(request)
        
        # Receive POST response from server
        response = seclab_socket.recv(1024)  
        print response
        
        # Send POST response to Alice.
        client_connection.send(response)
        
        # Close sockets.
        close_sockets()
