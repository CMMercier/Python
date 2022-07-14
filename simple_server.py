import socket
import threading

SRV_ADDR = input("Type the server IP address: ")
SRV_PORT = int(input("Type the server port: "))

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SRV_ADDR, SRV_PORT))
    s.listen(5)
    print(f'[*] Listening on {SRV_ADDR}:{SRV_PORT}')
    
    while True:
        client, address = s.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
