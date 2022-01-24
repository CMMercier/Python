import socket

SVR_ADDR = input("Type the server IP address: ")
SVR_PORT = int(input("Type the server port: "))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SVR_ADDR, SVR_PORT))
print("Connection established")

message = input("Message to send: ")
my_sock.sendall(message.encode())
my_sock.close()